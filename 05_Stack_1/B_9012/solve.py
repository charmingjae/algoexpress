import sys
n = int(sys.stdin.readline())

for i in range(n):
	lst = list(sys.stdin.readline().rstrip())
	cnt = 0
	printed = 0
	for j in range(len(lst)):
		if lst[j] == '(':
			cnt += 1
		elif lst[j] == ')':
			cnt -= 1
		if cnt < 0:
			print('NO')
			printed = 1
			break
	if printed == 0:
		if cnt == 0:
			print('YES')
		else:
			print('NO')