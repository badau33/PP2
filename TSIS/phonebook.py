import json, csv
from connect import connect

conn = connect()
cur = conn.cursor()
PAGE_SIZE = 5


def get_or_create_group(name):
    cur.execute("SELECT id FROM groups WHERE name=%s", (name,))
    g = cur.fetchone()
    if g:
        return g[0]
    cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (name,))
    return cur.fetchone()[0]


def add_contact():
    name = input("Name: ")
    email = input("Email: ") or None
    birthday = input("Birthday (YYYY-MM-DD): ") or None
    group = input("Group: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    gid = get_or_create_group(group)
    cur.execute(
        "INSERT INTO contacts(name,email,birthday,group_id) VALUES(%s,%s,%s,%s) RETURNING id",
        (name, email, birthday, gid)
    )
    cid = cur.fetchone()[0]
    cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)", (cid, phone, ptype))
    conn.commit()
    print("Added.")


def add_phone():
    name, phone, ptype = input("Name: "), input("Phone: "), input("Type: ")
    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))
    conn.commit()


def show_all():
    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name,
               STRING_AGG(p.phone || '(' || COALESCE(p.type,'?') || ')', ', ')
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
        GROUP BY c.id, g.name ORDER BY c.id
    """)
    for r in cur.fetchall():
        print(r)


def search():
    cur.execute("SELECT * FROM search_contacts(%s)", (input("Query: "),))
    for r in cur.fetchall():
        print(r)


def filter_by_group():
    cur.execute("""
        SELECT c.name, c.email, STRING_AGG(p.phone, ', ')
        FROM contacts c
        JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
        WHERE g.name=%s GROUP BY c.id
    """, (input("Group: "),))
    for r in cur.fetchall():
        print(r)


def search_by_email():
    cur.execute(
        "SELECT name, email FROM contacts WHERE email ILIKE %s",
        (f"%{input('Email keyword: ')}%",)
    )
    for r in cur.fetchall():
        print(r)


def sort_filter():
    g = input("Group (blank=all): ")
    sort = {"name": "c.name", "birthday": "c.birthday", "date": "c.created_at"}.get(
        input("Sort (name/birthday/date): "), "c.name"
    )
    q = "SELECT c.name,c.email,c.birthday,g.name FROM contacts c LEFT JOIN groups g ON c.group_id=g.id"
    params = []
    if g:
        q += " WHERE g.name=%s"
        params.append(g)
    cur.execute(q + f" ORDER BY {sort}", params)
    for r in cur.fetchall():
        print(r)


def pagination():
    page = 0
    while True:
        cur.execute(
            "SELECT c.name,c.email,c.birthday,g.name FROM contacts c LEFT JOIN groups g ON c.group_id=g.id ORDER BY c.id LIMIT %s OFFSET %s",
            (PAGE_SIZE, page * PAGE_SIZE)
        )
        rows = cur.fetchall()
        print(f"\n-- Page {page+1} --")
        for r in rows:
            print(r)
        cmd = input("next/prev/quit: ")
        if cmd == "next" and rows:
            page += 1
        elif cmd == "prev" and page > 0:
            page -= 1
        elif cmd == "quit":
            break


def move_to_group():
    cur.execute("CALL move_to_group(%s,%s)", (input("Name: "), input("Group: ")))
    conn.commit()


def delete_contact():
    cur.execute("DELETE FROM contacts WHERE name=%s", (input("Name: "),))
    conn.commit()
    print(f"Deleted {cur.rowcount}.")


def export_json():
    cur.execute("""
        SELECT c.name, c.email, c.birthday::TEXT, g.name,
               COALESCE(JSON_AGG(JSON_BUILD_OBJECT('phone',p.phone,'type',p.type)) FILTER (WHERE p.id IS NOT NULL),'[]')
        FROM contacts c
        LEFT JOIN groups g ON c.group_id=g.id
        LEFT JOIN phones p ON c.id=p.contact_id
        GROUP BY c.id, g.name
    """)
    data = [{"name": r[0], "email": r[1], "birthday": r[2], "group": r[3], "phones": r[4]} for r in cur.fetchall()]
    with open("contacts.json", "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Exported {len(data)}.")


def import_json():
    try:
        data = json.load(open(input("File (contacts.json): ") or "contacts.json"))
    except FileNotFoundError:
        return print("File not found.")

    for item in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (item["name"],))
        ex = cur.fetchone()
        if ex:
            if input(f"{item['name']} exists — skip/overwrite? ") != "overwrite":
                continue
            cur.execute("DELETE FROM contacts WHERE id=%s", (ex[0],))

        gid = get_or_create_group(item["group"]) if item.get("group") else None
        cur.execute(
            "INSERT INTO contacts(name,email,birthday,group_id) VALUES(%s,%s,%s,%s) RETURNING id",
            (item["name"], item.get("email"), item.get("birthday"), gid)
        )
        cid = cur.fetchone()[0]
        for p in item.get("phones", []):
            cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)", (cid, p["phone"], p["type"]))
    conn.commit()
    print("Import done.")


def import_csv():
    try:
        f = open(input("CSV file (contacts.csv): ") or "contacts.csv", newline="")
    except FileNotFoundError:
        return print("File not found.")

    for row in csv.DictReader(f):
        cur.execute("SELECT id FROM contacts WHERE name=%s", (row["name"],))
        if cur.fetchone():
            print(f"Skip: {row['name']}")
            continue
        gid = get_or_create_group(row["group"]) if row.get("group") else None
        cur.execute(
            "INSERT INTO contacts(name,email,birthday,group_id) VALUES(%s,%s,%s,%s) RETURNING id",
            (row["name"], row.get("email"), row.get("birthday"), gid)
        )
        cid = cur.fetchone()[0]
        if row.get("phone"):
            cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)", (cid, row["phone"], row.get("type", "mobile")))
    conn.commit()
    f.close()
    print("CSV import done.")


MENU = {
    "1":  ("Add contact",     add_contact),
    "2":  ("Add phone",       add_phone),
    "3":  ("Show all",        show_all),
    "4":  ("Search",          search),
    "5":  ("Filter by group", filter_by_group),
    "6":  ("Search by email", search_by_email),
    "7":  ("Sort + filter",   sort_filter),
    "8":  ("Pagination",      pagination),
    "9":  ("Move to group",   move_to_group),
    "10": ("Delete",          delete_contact),
    "11": ("Export JSON",     export_json),
    "12": ("Import JSON",     import_json),
    "13": ("Import CSV",      import_csv),
}

while True:
    print("\n" + "\n".join(f"{k}. {v[0]}" for k, v in MENU.items()) + "\n0. Exit")
    c = input("> ")
    if c == "0":
        break
    if c in MENU:
        try:
            MENU[c][1]()
        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")

cur.close()
conn.close()