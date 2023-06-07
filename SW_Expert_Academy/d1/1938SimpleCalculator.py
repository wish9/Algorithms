ip = list(map(int, input().split()))

x = ip[0]
y = ip[1]

print("%d\n%d\n%d\n%d" % (x+y, x-y, x*y, x//y))