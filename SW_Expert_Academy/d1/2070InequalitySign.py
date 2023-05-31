T = int(input())

for t in range(1, T + 1):
    values = list(map(int, input().split()))
    x = values[0]
    y = values[1]
    if(x<y) :
        print("#%s <" %str(t))
    elif(x==y) :
        print("#%s =" %str(t))
    else :
        print("#%s >" %str(t))