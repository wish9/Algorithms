ip = int(input())
# def solution(n):
#     answer = []
#     n=str(n)
#     for i in range(len(n)-1, -1, -1):
#         answer.append(int(n[i]))
#     return answer

"""
아래 방법 해설

1. 입력 정수를 문자열로 변환하고
2. 해당 문자를 반복(for)문으로 각 문자를 다시 정수로 변환해서 list형태로 저장하고
3. list에 있는 요소의 순서를 반대로 뒤집고 반전된 목록을 결과로 반환
"""
def solution(n):
    return [int(i) for i in str(n)][::-1]


print(solution(ip))