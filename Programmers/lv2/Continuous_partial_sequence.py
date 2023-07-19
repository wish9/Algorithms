def solution(elements):
    arr = []
    len_of_elements = len(elements)

    for i in range(1, len_of_elements+1):
        for j in range(len_of_elements):
            end = j+i
            if end > len_of_elements-1:
                end -= len_of_elements
                x = sum(elements[j:len_of_elements]) + sum(elements[0:end])
            else:
                x = sum(elements[j:end])

            if not arr.__contains__(x):
                arr.append(x)
                arr.sort()

    return len(arr)

print(solution([7,9,1,1,4]))