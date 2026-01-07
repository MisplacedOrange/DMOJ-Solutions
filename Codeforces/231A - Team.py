# Source: https://usaco.guide/general/io

def main():
    foo = int(input())
    count = 0
    for i in range(foo):
        p, v, t = map(int, input().split())
        if p+v+t > 1:
            count += 1
        else:
            pass
    print(count)
main()
