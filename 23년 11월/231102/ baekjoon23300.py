import sys

input = sys.stdin.readline


def compress(pages):
    result = [pages[0]]
    for i in range(1, len(pages)):
        if pages[i] != pages[i - 1]:
            result.append(pages[i])
    return result


n, q = map(int, input().split())

backward = []
forward = []
curr = ""
for _ in range(q):
    command = list(input().split())
    if command[0] == "B":  # Backward
        if backward:
            if curr:
                forward = [curr] + forward
            curr = backward.pop()
    elif command[0] == "F":  # Forward
        if forward:
            backward.append(curr)
            curr = forward.pop(0)
    elif command[0] == "C":  # Compress
        if backward:
            backward = compress(backward)
    else:  # Access
        if curr:
            backward.append(curr)
        curr = command[1]
        forward = []

print(curr)

if backward:
    print(*backward[::-1])
else:
    print(-1)

if forward:
    print(*forward)
else:
    print(-1)
