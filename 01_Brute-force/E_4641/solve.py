while True:
	s = list(map(int, input().split()))
	if len(s) == 1 and s[0] == -1:
		break
	cnt = 0
	for i in s:
		if i == 0:
			break
		if i * 2 in s:
			cnt += 1
	print(cnt)