#    A            B     answer
# [1, 4, 2]   [5, 4, 4]	  29
#  [1,2]	    [3,4]     10

ip1 = list(map(int, input().split()))
ip2 = list(map(int, input().split()))

def solution(A,B):
    answer = 0

    for i in range(len(A)):
        answer += min(A)*max(B)
        A.remove(min(A))
        B.remove(max(B))

    return answer

print(solution(ip1, ip2))