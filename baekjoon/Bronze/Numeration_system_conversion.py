N, B = input().split(" ")
def solution(N, B):
    B = int(B)
    conversion_value = 0
    digit = len(N)

    for i in range(digit):
        unicode = ord(N[i])

        if unicode >= 65:
            exponent = unicode - 55
        else:
            exponent = unicode - 48

        conversion_value += exponent * B ** (digit - 1 - i)

    return conversion_value

print(solution(N, B)) # "ZZZZZ 36"