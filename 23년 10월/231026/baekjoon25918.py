import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().strip()

    cnt = 0
    max_cnt = 0

    for i in S:
        if i == "(":
            cnt += 1
        else:
            cnt -= 1

        if abs(cnt) > max_cnt:
            max_cnt = abs(cnt)

    if cnt != 0:
        print(-1)
    else:
        print(max_cnt)


if __name__ == "__main__":
    main()
