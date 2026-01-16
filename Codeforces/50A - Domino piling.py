import math
l, w = map(int, input().split())

A = l*w

dominos = A / 2
print(math.floor(dominos))