a, b = map(int, input().split())
c = int(input())

hour = (
    min(int((a * 60 + b + c) / 60), int((a * 60 + b + c) / 60) - 24)
    if int((a * 60 + b + c) / 60) >= 24
    else int((a * 60 + b + c) / 60)
)

minute = (a * 60 + b + c) % 60
print(str(hour) + " " + str(minute))
