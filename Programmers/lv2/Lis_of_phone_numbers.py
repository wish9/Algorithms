def solution(phone_book):
    answer = True

    sorted_phone_book = sorted(phone_book, key=len)

    for i in range(len(phone_book)-1):
        phone_num = sorted_phone_book[i]
        for j in range(i+1, len(phone_book)):
            if sorted_phone_book[j].startswith(phone_num):
                answer = False
                break
        if not answer:
            break

    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))