T = int(input())

def findPatternLength(str):
    nodes = str[0]
    result = 0

    for i in range(1, len(str)):
        if result == len(nodes):
            break

        if str[i] == nodes[0]:
            result += 1
            for j in range(1, len(nodes)):
                if str[i+j] == nodes[j]:
                    result += 1
                else:
                    result = 0
                    nodes += str[i]
                    break
        else:
            nodes += str[i]

    return result


for t in range(1, T + 1):
    ip = input()

    ans = findPatternLength(ip)

    print('#', t, ' ', ans, sep="")