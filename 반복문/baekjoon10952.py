# A, B = map(int, input().split())
# if not (A == 0 and B == 0):
#     print(A + B)


# while not (A == 0 and B == 0):
#     A, B = map(int, input().split())
#     if not (A == 0 and B == 0):
#         print(A + B)

while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    print(A + B)
