ip = int(input())

def collatz(num, count):

    if num%2==0: num = num/2
    else: num = num*3+1

    count += 1

    if int(num) == 1: return count
    elif count >= 500 or count == -1: return -1

    count = collatz(num, count)
    return count

def solution(num):
    if num==1: return 0
    count = 0
    answer = collatz(num, count)
    return answer

print(solution(ip))