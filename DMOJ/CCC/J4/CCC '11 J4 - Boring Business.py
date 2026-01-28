cords = {
    (0, -1), (0, -2), (0, -3),
    (1, -3), (2, -3), (3, -3), (3, -4), (3, -5),
    (4, -5), (5, -5), (5, -4), (5, -3),
    (6, -3), (7, -3), (7, -4), (7, -5), (7, -6), (7, -7),
    (6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7), (0, -7),
    (-1, -7), (-1, -6), (-1, -5)
}
x, y = -1, -5

while True:

    n = input()
    foo, num = n.split()
    num = int(num)

    if foo == 'q' and num == 0:
        break

    if foo in 'ruld':
        danger = False
        for _ in range(num):
            if foo == 'r': x += 1
            elif foo == 'l': x -= 1
            elif foo == 'u': y += 1
            elif foo == 'd': y -= 1

            if (x, y) in cords:
                danger = True
            cords.add((x, y))
    if danger:
        print(f"{x} {y} DANGER")
        break
    else:
        print(f"{x} {y} safe")