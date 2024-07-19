
n, m, k = map(int, input().split())
num = list(map(int, input().split()))
ans = 0
num.sort(reverse=True)

first = num[0]
second = num[1]

# 가장 큰수 수열이 더해지는 횟수 계산
cnt = int(m / (k+1)) * k
cnt += m % (k+1)

ans = cnt * first
ans += (m - cnt) * second


print(ans)


'''
5 8 3
2 4 5 4 6

TIP: 
- 가장 큰 수와 가장 작은 수만 저장
- 반복되는 수열 파악
'''