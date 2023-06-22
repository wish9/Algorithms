s = input()
Num_of_P = 0
Num_of_Y = 0

# for i in range(len(s)):
#     if s[i]=='P' or s[i]=='p': Num_of_P += 1
#     elif s[i]=='Y' or s[i]=='y': Num_of_Y += 1
#
# if Num_of_P == Num_of_Y: print(True)
# else: print(False)

def numPY(s):
    return s.lower().count('p') == s.lower().count('y') # 대소문자 상관 없이 카운팅 하기 위해 lower 사용

print(numPY(s))