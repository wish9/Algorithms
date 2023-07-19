def solution(elements):
    ans = 0
    result = list(set(elements))
    arr = [elements]
    len_of_elements = len(elements)

    for i in range(1, len_of_elements): # i = 수열의 길이
        arr_to_be_added = []
        previous_arr = arr[i-1]

        for j in range(len_of_elements):
            if j+i < len_of_elements:
                end = j+i
            else:
                end = j+i-len_of_elements
            value = previous_arr[j] + elements[end]
            arr_to_be_added.append(value)

            if not result.__contains__(value):
                result.append(value)

        arr.append(arr_to_be_added)

    return len(result)

def solution2(elements):
    result = []
    for i in range(len(elements)):
        arr = elements[i:len(elements)] + elements[0:i]
        add_value = 0
        for j in arr:
            add_value += j
            if not result.__contains__(add_value):
                result.append(add_value)

    return len(result)

print(solution([7,9,1,1,4]))
print(solution2([7,9,1,1,4]))