x, y = map(int, input().split())
a, b = map(int, input().split())

if y == b:
    print("x-axis")
elif x == a:
    print("y-axis")
else:
    print("neither")
