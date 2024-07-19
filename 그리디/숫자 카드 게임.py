'''
가장 낮은 숫자, 최종적으로 가장 높은 숫자의 카드를뽑는다.
N * M

Tip:
'''

n, m = map(int, input().split())
ans = 0
for i in range(m):
    data = list(map(int, input().split()))
    rowValue = min(data)
    ans = max(rowValue, ans)

print(ans)


'''
3 3

3 1 2 
4 1 4 
2 2 2
'''