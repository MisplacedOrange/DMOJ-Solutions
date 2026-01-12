operators = int(input())
count = 0

for i in range(operators):
    operations = input()
    if operations == "X++" or operations == "++X":
        count += 1
    elif operations == "--X" or operations == "X--":
        count -= 1
print(count)