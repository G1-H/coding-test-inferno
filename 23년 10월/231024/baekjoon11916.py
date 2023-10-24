import sys

input = sys.stdin.readline


def main():
    N = int(input())
    ball = list(map(int, input().split()))

    base1, base2, base3, score, cnt = False, False, False, 0, 0

    for x in ball:
        if x == 1:  # 볼
            if cnt == 3:  # 볼넷
                if base1 == False:  # 1루부터 확인
                    base1 = True
                    cnt = 0
                elif base2 == False:  # elif로 1루에 주자가 있는 경우로 제한하기
                    base2 = True
                    cnt = 0
                elif base3 == False:
                    base3 = True
                    cnt = 0
                else:
                    cnt = 0
                    score += 1
            else:  # 볼넷 X
                cnt += 1
        elif x == 2:  # 데드볼 = 볼넷
            if base1 == False:
                base1 = True
                cnt = 0
            elif base2 == False:
                base2 = True
                cnt = 0
            elif base3 == False:
                base3 = True
                cnt = 0
            else:
                cnt = 0
                score += 1
        elif x == 3:  # 폭투
            if cnt == 3:  # 폭투와 볼넷이 겹칠 경우
                if base3 == True:  # 3루부터 확인
                    base3 = False
                    score += 1
                if base2 == True:  # 볼넷과 데드볼과 다르게 제한 조건 존재 X, elif 사용 X
                    base2 = False
                    base3 = True
                if base1 == True:
                    base1 = False
                    base2 = True
                cnt = 0
                base1 = True
            else:  # 겹치지 않을 경우
                if base3 == True:
                    base3 = False
                    score += 1
                if base2 == True:
                    base2 = False
                    base3 = True
                if base1 == True:
                    base1 = False
                    base2 = True
                cnt += 1

    print(score)


if __name__ == "__main__":
    main()
