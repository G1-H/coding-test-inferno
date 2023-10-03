# 문제 : N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
#      다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
#      모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
# 출력 : M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

from bisect import bisect_left, bisect_right
import sys


n = int(sys.stdin.readline())
array = []
array = list(map(int, sys.stdin.readline().split()))


m = int(sys.stdin.readline())
array_x = []
array_x = list(map(int, sys.stdin.readline().split()))

array.sort()


# 재귀적 구현
def is_include(array, x, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == x:
        return 1
    elif array[mid] < x:
        start = mid + 1
        return is_include(array, x, start, end)
    else:
        end = mid - 1
        return is_include(array, x, start, end)


for i in array_x:
    print(is_include(array, i, 0, len(array) - 1))

# 메모리 140024KB	시간 444ms


# 반복문 구현
def is_include(array, x, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == x:
            return 1
        elif array[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return 0


for i in array_x:
    print(is_include(array, i, 0, len(array) - 1))

# 메모리 140028KB	 시간 268ms


# 파이썬 이진 탐색 라이브러리 : bisect_left
# bisect_left(array, x) -> x를 array 에 정렬을 유지하면서 넣었을 때, 가장 왼쪽 인덱스
def is_include(array, x):
    clue = bisect_left(array, x)
    if clue == len(array):
        return 0
    if x == array[clue]:
        return 1
    else:
        return 0


for i in array_x:
    print(is_include(array, i))

# 	메모리 : 140028KB 	시간 : 312ms


# 파이썬 이진 탐색 라이브러리 : bisect_right
# bisect_right(array, x) -> x를 array 에 정렬을 유지하면서 넣었을 때, 가장 오른쪽 인덱스
def is_include(array, x):
    clue = bisect_right(array, x)
    if clue == 0:
        return 0
    if x == array[clue - 1]:
        return 1
    else:
        return 0


for i in array_x:
    print(is_include(array, i))

# 	메모리 : 140028KB	시간 : 288ms
