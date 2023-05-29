for i in range(10) :
    print(i, end=' ');

print()

for i in range(0,10) :
    print(i, end=' ');

num = 10
day = "three"
a = "I ate %s apples. so I was sick for %s days." % (num, day)
print(a)
print(a[-1]) #맨 뒷글자

print("I ate %s apples.\nso I was sick for %s days." % (num, day))

a="Life is too short"
print(a.replace("Life","Your leg"))

a = ",".join("abcd")  # abcd에 , 문자열 삽입
print(a)

a = "%3s" % "hi"  # "hi"를 3자의 너비로 형식화, "hi"는 2글자이므로 "hi" 앞에 공백을 하나 추가하여 총 3글자를 만든다.
print(a)

a = "%8.4f" % 3.42135234   # 총 8자의 너비로 형식화, 정밀도 = 소수점4자리
print(a)
print(ord('b'))
print(a.find("421"))