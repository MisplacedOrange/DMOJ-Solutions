n, score = map(int, input().split())
count = 0
    
scores = list(map(int, input().split()))
    
for i, j in enumerate(scores):
    
    if j > 0:
        if j >= scores[score - 1]:
            count += 1
print(count)