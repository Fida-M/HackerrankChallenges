n = int(input())
s = set(map(int, input().split()))
number_command = int(input())
commands=[]
for _ in range(number_command):
    command=input().split()  
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif  command[0] == "discard":
        s.discard(int(command[1])) 
result=0
for i in s:
    result+=i
print(result)
