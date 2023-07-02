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

print(solution(ip))