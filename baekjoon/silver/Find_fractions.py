def solution(X):
    total = 1
    list_len = 1
    max_num = 1

    while total < X:
        list_len += 1
        total += list_len
        max_num += 1

    if max_num % 2 == 0:
        return "%d/%d" %(max_num - (total - X), 1 + (total - X))
    else:
        return "%d/%d" %(1 + (total - X), max_num - (total - X))

print(solution(int(input())))