def fail(phone_book):
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

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))