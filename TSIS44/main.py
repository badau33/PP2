import pygame, sys, random, json
from db import save_score, get_top_10

pygame.init()

W, H = 800, 600
CELL = 20

win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 28)
small = pygame.font.SysFont("Verdana", 20)

try:
    config = json.load(open("settings.json"))
except:
    config = {"snake_color": [66,165,245], "grid": True}

user_name = ""
state = "MENU"

class Game:
    def __init__(self, name):
        self.name = name
        self.snake = [(120,120),(100,120),(80,120)]
        self.dir = (CELL,0)
        self.score = 0
        self.level = 1
        self.speed = 10
        self.obstacles = []
        self.food = self.spawn()
        self.poison = self.spawn()
        self.power = None
        self.power_type = None
        self.active_power = None
        self.power_end = 0
        self.shield = False
        self.spawn_obstacles()

    def spawn(self):
        while True:
            x = random.randrange(0,W,CELL)
            y = random.randrange(0,H,CELL)
            if (x,y) not in self.snake and (x,y) not in self.obstacles:
                return (x,y,random.randint(1,3))

    def spawn_obstacles(self):
        self.obstacles = []
        if self.level >= 3:
            for _ in range(self.level*3):
                while True:
                    x = random.randrange(0,W,CELL)
                    y = random.randrange(0,H,CELL)
                    if (x,y) not in self.snake:
                        self.obstacles.append((x,y))
                        break

    def spawn_power(self):
        x = random.randrange(0,W,CELL)
        y = random.randrange(0,H,CELL)
        self.power = (x,y)
        self.power_type = random.choice(["SPEED","SLOW","SHIELD"])

    def update(self):
        now = pygame.time.get_ticks()

        if self.active_power and now > self.power_end:
            self.speed = 10 + self.level * 2
            self.active_power = None
            self.shield = False

        x,y = self.snake[0]
        nx,ny = x+self.dir[0], y+self.dir[1]
        new = (nx,ny)

        if nx<0 or ny<0 or nx>=W or ny>=H:
            return False

        if new in self.snake or new in self.obstacles:
            if self.shield:
                self.shield = False
            else:
                return False

        self.snake.insert(0,new)

        if new==(self.food[0],self.food[1]):
            self.score += self.food[2]
            if self.score // 5 > self.level - 1:
                self.level += 1
                self.speed += 2
                self.spawn_obstacles()
            self.food = self.spawn()

        elif new==(self.poison[0],self.poison[1]):
            if len(self.snake)<=3:
                return False
            self.snake = self.snake[:-2]
            self.poison = self.spawn()

        elif self.power and new==self.power:
            self.active_power = self.power_type
            self.power_end = now + 5000

            if self.power_type=="SPEED":
                self.speed = 20
            elif self.power_type=="SLOW":
                self.speed = 5
            elif self.power_type=="SHIELD":
                self.shield = True

            self.power = None

        else:
            self.snake.pop()

        if not self.power and random.random()<0.01:
            self.spawn_power()

        return True

game = None

def button(text,x,y,w,h):
    mx,my = pygame.mouse.get_pos()
    rect = pygame.Rect(x,y,w,h)
    clicked = False

    pygame.draw.rect(win,(255,255,255),rect,border_radius=10)
    pygame.draw.rect(win,(0,0,0),rect,2,border_radius=10)

    if rect.collidepoint(mx,my):
        pygame.draw.rect(win,(255,220,120),rect,border_radius=10)
        if pygame.mouse.get_pressed()[0]:
            clicked = True

    win.blit(small.render(text,True,(0,0,0)),(x+20,y+15))
    return clicked

def menu(events):
    global state, game, user_name

    win.fill((30,30,40))
    win.blit(font.render("SNAKE GAME",True,(255,255,255)),(280,100))
    win.blit(small.render(f"Player: {user_name}_",True,config["snake_color"]),(320,170))

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_name = user_name[:-1]
            elif event.key == pygame.K_RETURN:
                if user_name:
                    game = Game(user_name)
                    state = "GAME"
            else:
                if len(user_name)<12 and event.unicode.isprintable():
                    user_name += event.unicode

    if button("PLAY",300,250,200,50) and user_name:
        game = Game(user_name)
        state = "GAME"

    if button("LEADERBOARD",300,320,200,50):
        state = "LEAD"

    if button("SETTINGS",300,390,200,50):
        state = "SET"

def game_loop():
    global state

    win.fill((240,240,240))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and game.dir!=(0,CELL):
        game.dir=(0,-CELL)
    if keys[pygame.K_DOWN] and game.dir!=(0,-CELL):
        game.dir=(0,CELL)
    if keys[pygame.K_LEFT] and game.dir!=(CELL,0):
        game.dir=(-CELL,0)
    if keys[pygame.K_RIGHT] and game.dir!=(-CELL,0):
        game.dir=(CELL,0)

    if not game.update():
        try:
            save_score(game.name,game.score,game.level)
        except:
            pass
        state="MENU"

    for s in game.snake:
        pygame.draw.rect(win,config["snake_color"],(s[0],s[1],CELL,CELL))

    for o in game.obstacles:
        pygame.draw.rect(win,(50,50,50),(o[0],o[1],CELL,CELL))

    if game.power:
        pygame.draw.rect(win,(255,215,0),(game.power[0],game.power[1],CELL,CELL))

    pygame.draw.rect(win,(0,200,0),(game.food[0],game.food[1],CELL,CELL))
    pygame.draw.rect(win,(150,0,0),(game.poison[0],game.poison[1],CELL,CELL))

    win.blit(font.render(f"Score: {game.score}",True,(0,0,0)),(10,10))

    if game.active_power:
        win.blit(small.render(f"{game.active_power}",True,(255,140,0)),(650,10))

def leaderboard():
    global state

    win.fill((10,10,10))
    win.blit(font.render("LEADERBOARD",True,(255,255,255)),(300,50))

    try:
        top = get_top_10()
    except:
        top = []

    y=120
    for i,r in enumerate(top[:10]):
        try:
            win.blit(small.render(f"{i+1}. {r[0]} - {r[1]}",True,(255,255,255)),(300,y))
        except:
            pass
        y+=30

    if button("BACK",320,500,150,40):
        state="MENU"

def settings():
    global state, config

    win.fill((220,220,220))
    win.blit(font.render("SETTINGS",True,(0,0,0)),(330,80))

    if button(f"GRID: {config['grid']}",300,200,220,50):
        config["grid"]=not config["grid"]

    if button("CHANGE COLOR",300,270,220,50):
        config["snake_color"]=[random.randint(50,255),random.randint(50,255),random.randint(50,255)]

    if button("SAVE & BACK",300,340,220,50):
        json.dump(config,open("settings.json","w"))
        state="MENU"

while True:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if state=="MENU":
        menu(events)
    elif state=="GAME":
        game_loop()
    elif state=="LEAD":
        leaderboard()
    elif state=="SET":
        settings()

    pygame.display.update()
    clock.tick(15)