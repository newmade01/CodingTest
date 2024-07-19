'''
1. 각 행마다 작은수를 찾음
2. 작은 수중 가장 큰 수가 답

3 3
3 1 2
4 1 4
2 2 2
'''


n, m =map(int, input().split())
result = 0
minv= 0

for i in range(n):
    data = list(map(int, input().split()))
    minv = min(data)

    result = max(result, minv ) #  주의

print(result)
