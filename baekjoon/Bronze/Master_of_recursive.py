T = int(input())
for _ in range(T):
    def recursion(s, l, r, count):
        if l >= r:
            return 1, count
        elif s[l] != s[r]:
            return 0, count
        else:
            count += 1
            return recursion(s, l + 1, r - 1, count)
    def isPalindrome(s):
        count = 1
        return recursion(s, 0, len(s) - 1, count)

    ip = input()
    answer = isPalindrome(ip)
    print(str(answer[0]) + " " + str(answer[1]))