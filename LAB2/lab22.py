n,i,j=map(int,input().split())
numbers=list(map(int, input().split()))
numbers[i-1:j]=reversed(numbers[i-1:j])
print(*numbers)