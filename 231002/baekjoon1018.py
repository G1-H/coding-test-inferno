n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(input())

answer = 64

for s_x in range(n - 7):
    for s_y in range(m - 7):
        paint_standard_as_first = 0
        paint_standard_as_first_opposite = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if board[s_x][s_y] != board[s_x + x][s_y + y]:
                        paint_standard_as_first += 1
                    else:
                        paint_standard_as_first_opposite += 1

                else:
                    if board[s_x][s_y] == board[s_x + x][s_y + y]:
                        paint_standard_as_first += 1
                    else:
                        paint_standard_as_first_opposite += 1
        answer = min(answer, paint_standard_as_first, paint_standard_as_first_opposite)


print(answer)

# 왼쪽 최상단의 수에 맞춰 나머지 색을 변경하도록만 구성하여 모든 경우의 수를 확인하지 않았다.
# 왼쪽 최상단의 수가 변경되었을 경우도 생각하여 코드를 작성하여야 했다.
