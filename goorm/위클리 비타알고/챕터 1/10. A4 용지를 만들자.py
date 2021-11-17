cnt = 0 # 만들 수 있는 A4용지 수
n, m = map(int, input().split())
# m이 항상 크도록 설정
if n > m:
	tmp = n
	n = m
	m = tmp

# 짧은 쪽을 20cm, 긴 쪽을 40cm으로 최대한 A4용지를 만든다
cnt += (n // 20) * (m // 40)

# 남은 쪽으로 A4용지를 더 만들 수 있다면 만든다
m -= (m // 40) * 40
if m >= 20:
	cnt += n // 40
	
print(cnt)
