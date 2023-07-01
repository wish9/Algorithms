#    A            B     answer
# [1, 4, 2]   [5, 4, 4]	  29
#  [1,2]	    [3,4]     10

ip1 = list(map(int, input().split()))
ip2 = list(map(int, input().split()))

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer

print(solution(ip1, ip2))