# import sys
# sys.stdin.readline() 이 input() 보다 속도에서 우위를 보인다.
# why?
# 한번에 읽어와 버퍼에  저장하는 stdin.readline()가 하나씩 누를 때마다 데이터를 버퍼에 보관하는 input() 보다 처리 속도가 빠르다. 즉, 버퍼 사이즈 차이로 입력이 반복될 수록 stdin.readline()이 우위를 가진다.

n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
list.sort()
# list 자체를 정렬 -> list.sort  기본 오름차순///
# 내림차순 -> list.sort(reverse=True)
# list를 정렬해 새로운 리스트   -> list2 = sorted(list) // 여기서 내림차순으로 하려면 정렬한 리스트 다시 reverse 해야함.
# ex. list2 = sorted(list) // list2.reverse()
for i in list:
    print(i)
