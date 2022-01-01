n = int(input())
cnt = 0
a = 1
while True:
	if '666' in str(a):
		cnt += 1
	if cnt == n:
		print(a)
		break
	a += 1