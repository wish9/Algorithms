T=int(input())

for t in range(1, T+1):
    ip = list(map(int, input().split()))
    print("#%d %d %d" %(t, ip[0]//ip[1], ip[0]%ip[1]))