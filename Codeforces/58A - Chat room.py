hello = []
seperator = ''
foo = input()

for i in foo:
    if i == 'h' and hello == []:
        hello.append(i)
    elif i == 'e' and hello == ['h']:
        hello.append(i)
    elif i == 'l' and hello == ['h', 'e']:
        hello.append(i)
    elif i == 'l' and hello == ['h', 'e', 'l']:
        hello.append(i)
    elif i == 'o' and hello == ['h', 'e', 'l', 'l']:
        hello.append(i)
    else:
        pass
if seperator.join(hello) == "hello":
    print("YES")
else:
    print("NO")