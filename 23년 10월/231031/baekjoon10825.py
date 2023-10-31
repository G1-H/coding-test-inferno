import sys

input = sys.stdin.readline

n = int(input())

students = []
for _ in range(n):
    student = list(input().split())
    name = student[0]
    korean = int(student[1])
    english = int(student[2])
    math = int(student[3])
    students.append((-korean, english, -math, name))

students.sort()

for s in students:
    print(s[3])
