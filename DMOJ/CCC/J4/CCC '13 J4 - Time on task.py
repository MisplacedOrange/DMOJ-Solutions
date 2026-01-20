t = int(input())
n = int(input())

chores = sorted(int(input()) for _ in range(n))
cnt = 0
for chore in chores:
    if t >= chore:
        t -= chore
        cnt += 1
    else:
        break

print(cnt)
