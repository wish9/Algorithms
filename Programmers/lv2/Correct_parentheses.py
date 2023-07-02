import queue
from collections import deque

ip = input()

def solution(s):
    s = deque(s)
    openCounting = deque()
    while len(s)!=0:
        left = s.popleft()
        if left == '(': openCounting.append('(')
        elif left == ')':
            if len(openCounting) == 0:
                return False
            openCounting.pop()

    if len(s) ==0 and len(openCounting)!=0: return False
    return True

def solution2(s):
    pair = 0
    for x in s:
        if pair < 0: return False
        pair = pair +1 if x == '(' else pair -1
    return pair == 0

print(solution(ip))
print(solution2(ip))