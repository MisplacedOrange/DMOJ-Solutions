n = int(input())

for i in range(n):
    foo = input().strip()
    cnt = 1

    list = []
    for i in range(1, len(foo)):
        if foo[i] == foo[i-1]:
            cnt+=1
        else:
            list.append(f"{cnt} {foo[i-1]}")
            cnt = 1

    list.append(f"{cnt} {foo[-1]}")

    print(' '.join(list))
