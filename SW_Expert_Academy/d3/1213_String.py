# for _ in range(10):
#     t = int(input())
#     searchS = input()
#     S = input()
#     result = 0
#
#     for i in range(len(S)-len(searchS)+1):
#         isSame = True
#         for j in range(len(searchS)):
#             if S[i+j] != searchS[j]:
#                 isSame = False
#                 break
#             else:
#                 isSame = True
#         if isSame:
#             result += 1
#
#     print('#', t, ' ', result, sep='')

for _ in range(10):
    t = int(input())
    searchS = input()
    S = input()
    result = 0

    for i in range(len(S) - len(searchS) + 1):
        if S[i:i+len(searchS)] == searchS:
            result += 1

    print('#', t, ' ', result, sep='')
