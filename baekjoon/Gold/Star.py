def star(N):
    if N == 1:
        return "*"
    else:
        result = star(N // 3)
        top_bottom = [line * 3 for line in result]
        middle = [line + ' ' * (N // 3) + line for line in result]
        return top_bottom + middle + top_bottom

pattern = star(int(input()))
for line in pattern:
    print(line)