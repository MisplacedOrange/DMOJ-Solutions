a, b, c, d = map(int, input().split())

calc = [0, a, a + b, a + b + c, a + b + c + d]

for i in range(5):
    row = []
    for j in range(5):
        row.append(str(abs(calc[j] - calc[i])))
    print(" ".join(row))
