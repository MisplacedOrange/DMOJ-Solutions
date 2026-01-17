n, m, a, b = map(int, input().split())
print(min((n*a), (b * (n//m) + min((n%m)*a, b))))