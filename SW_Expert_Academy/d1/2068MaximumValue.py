T = int(input())
count = 0;

for test_case in range(1, T + 1):
    count += 1
    values = list(map(int, input().split()))
    print("#" + str(count) + " " + str(max(values)))