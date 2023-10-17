# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


N = int(input())

# 각 줄에서 퀸이 위치할 위치를 나타낸 리스트
row = [0 for _ in range(N)]
# 퀸이 위치할 수 있는 경우의 수 카운트할 cnt
cnt = 0


def check(x):
    for i in range(x):
        if row[i] == row[x] or x - i == abs(row[x] - row[i]):
            return False
    return True


def n_queen(x):
    global cnt
    if x == N:
        cnt += 1
        return
    for i in range(N):
        row[x] = i

        if check(x):
            n_queen(x + 1)


n_queen(0)
print(cnt)
