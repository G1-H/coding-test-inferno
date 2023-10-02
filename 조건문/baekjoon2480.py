a, b, c = map(int, input().split())
if a == b and b == c:
    print(a * 1000 + 10000)
elif (a == b or a == c) and b != c:
    print(a * 100 + 1000)
elif (b == c) and a != b:
    print(b * 100 + 1000)
else:
    print(max(a, b, c))


# a, b, c = map(int, input().split())
# print(a, b, c)
# array1 = [a, b, c]
# array2 = list(set(array1))
# array3 = array1 + array2
# array3.sort()

# print(array1)
# print(array1 + array2)

# if len(array2) == 1:
#     print(10000 + array3[3] * 1000)
# elif len(array2) == 2:
#     print(1000 + array3[2] * 100)
# else:
#     print(array3[5] * 100)
