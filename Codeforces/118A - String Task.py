# Source: https://usaco.guide/general/io

def main():
    foo = input().lower()
    letters = []
    for x in foo:
        if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u' or x == 'y'):
            pass
        else:
            letters.append(x)
    seperator = '.'
    print(f".{seperator.join(letters)}")
main()
