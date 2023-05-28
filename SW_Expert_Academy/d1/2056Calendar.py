T = int(input())

for test_case in range(1, T + 1):
    t = input()
    maxDay = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    m=str(t)[4:6]
    m2=int(m)
    if m2>12 or m2==0:
        print("#%s" %str(test_case), -1)
    elif m2>0:
        d=str(t)[6:8]
        if 0<int(d)<=maxDay[m2]:
            print("#%d" %test_case,"%s/%s/%s" %(str(t)[0:4],m,d))
        else :print("#%s" %str(test_case), -1)

# 5
# 22220228
# 20150002
# 01010101
# 20140230
# 11111111

