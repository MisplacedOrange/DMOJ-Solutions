n = input()

while n != '0':
    prefix = n.split()
    postfix = []
    for char in reversed(prefix):
        if char not in '+-':
            postfix.append(char)
        else:
            a = postfix.pop()
            b = postfix.pop()
            postfix.append(f'{a} {b} {char}')
    print(postfix[0])
    n = input()


        

