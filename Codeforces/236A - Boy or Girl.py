from collections import Counter

n = input().strip()

odd = 0
    
cnt = Counter(n)
for i, j in cnt.items():
    odd+=1

if (odd % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")