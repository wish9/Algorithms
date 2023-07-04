ip = int(input())

def solution(n):
    binaryN = bin(n)[2:]

    min_index_1 = binaryN.rfind('1')
    i = 1
    while binaryN[min_index_1-i] == '1':
        i += 1
        if min_index_1-i==-1: break

    need_replace_part = binaryN[min_index_1-i+1:]
    num_of_1 = need_replace_part.count('1')
    num_of_0 = need_replace_part.count('0')

    changed = '1' + '0'*(num_of_0+1) + '1'*(num_of_1-1)

    if min_index_1-i != -1:
        answer = binaryN[0:min_index_1-i] + changed
    else:
        answer = changed

    return int(answer, 2)

print(solution(ip))