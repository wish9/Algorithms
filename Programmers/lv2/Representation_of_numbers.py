ip = int(input())

def solution(n):
    answer = 0
    for i in range(1, n//2 + 1, 2):
        if n % i ==0:
            answer += 1

    if n%2==1: answer+= 1
    return answer

'''
n 이하인 숫자 a부터 k개의 연속된 숫자의 합이 n이라고 가정

a + (a+1) + (a+2) + ... + (a+k-1) = k(2a+k-1)/2 = n
a <= n
k < n
a,k : 자연수

a = n/k + (1-k)/2 #등차수열 합공식
a가 자연수기 때문에
n/k 가 자연수이려면 : k는 n의 약수여야 한다.
(1-k)/2 가 정수가 되려면 : 1-k 가 짝수여야 하므로 k는 홀수여야 한다.
따라서 k가 n의 약수이면서 n보다 작은 홀수일 때 a는 자연수가 된다. (k < n)
또한 n이 홀수라면 k=2일 때 무조건 a는 자연수가 된다.

따라서 n이 짝수일 경우 n의 약수 중 홀수인 갯수
n이 홀수일 경우 n의 약수 중 홀수인 갯수 -1 +1 을 구하면 되기 떄문에

결론적으로 n의 짝수 홀수 여부에 상관없이 n의 약수 중 홀수인 요소들의 갯수를 구하면 된다.
'''

print(solution(ip))