'''
500x, 100y, 50z , 10k

N원 =>500x + 100y + 50z + 10k
ans: 동전의 최소 갯수는?

N: 10의 배수
'''
N = 1260
ans = 0
coin = [500, 100, 50, 10]

for i in coin:
    ans += (N // i)
    N %= i

print(ans)

'''
거슬러줄 코인 타입에만 영향을 받음
'''