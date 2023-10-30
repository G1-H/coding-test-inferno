answer = 0
n = 0
N = int(input())

while n != N:
    answer += 1
    string = str(answer)
    if "666" in string:
        n += 1

print(answer)
