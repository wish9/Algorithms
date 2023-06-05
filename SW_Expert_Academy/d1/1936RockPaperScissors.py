values = list(map(int, input().split()))

# if values[0]<values[1]:
#     if values[1]==2 or values[0]==2: print('B')
#     else: print('A')
# else:
#     if values[0]==2 or values[1]==2 : print('A')
#     else: print('B')

if (values[1]-values[0]+3) % 3 == 1:
    print('B')
else:
    print('A')