s = input()
Num_of_P = 0
Num_of_Y = 0


for i in range(len(s)):
    if s[i]=='P' or s[i]=='p': Num_of_P += 1
    elif s[i]=='Y' or s[i]=='y': Num_of_Y += 1

if Num_of_P == Num_of_Y: print(True)
else: print(False)