total = int(input())
N = int(input())
for x in range(N):
    a, b = map(int, input().split())

    total -= a * b

if not (total):
    print("Yes")
else:
    print("No")
