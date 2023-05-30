n=int(input())
values = list(map(int,input().split()))
values.sort()
print(values[(n-1)//2])