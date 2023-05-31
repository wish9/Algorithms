T = int(input())

for t in range(1, T + 1):
    x, y = map(int, input().split())
    print("#%d" %(t), end=' ')
    if x < y:
        print("<")
    elif x == y:
        print("=")
    else:
        print(">")