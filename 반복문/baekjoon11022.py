import sys

N = sys.stdin.readline().rstrip()

for x in range(int(N)):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(f"Case #{x+1}: {A} + {B} = {A+B}")
