# Source: https://usaco.guide/general/io
import math

def main():
    foo = int(input().strip())
    if foo % 2 == 0 and foo > 2:
        print("YES")
    else:
        print("NO")
main()