# Source: https://usaco.guide/general/io
import math

def main():
    foo = int(input())
    for i in range(foo):
        wrd = str(input().strip())
        if len(wrd) <= 10:
            print(wrd)
        else:
            print(f"{wrd[0]}{len(wrd)-2}{wrd[-1]}")
main()