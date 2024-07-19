'''
m번 더하기
k번 초과 연속 불가능
n 배열크기

5 8 3
2 4 5 4 6
'''
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data = data.sort()
index = n - 1
re = 0

for _ in range(m):
    for _ in range(k):
        re += data[index]

    index -= 1

print(re)
