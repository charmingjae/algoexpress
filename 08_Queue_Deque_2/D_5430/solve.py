from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
	printed = 0
	# 함수들
	command = deque(sys.stdin.readline().rstrip())
	# 수의 개수
	n = int(sys.stdin.readline())
	# 수들
	nbr = deque((sys.stdin.readline().rstrip().strip('[]')).split(','))
	if n == 0:
		nbr = deque()
	# 리턴 값
	command_reverse = 0
	for i in command:
		# Reverse
		if i == 'R':
			command_reverse += 1
		elif i == 'D':
			if not nbr :
				print('error')
				printed = 1
				break
			if command_reverse % 2 == 1:
				nbr.pop()
			else:
				nbr.popleft()
	if printed == 0:
		if command_reverse % 2 == 1:
			nbr.reverse()
			print('[' + ','.join(nbr) + ']')
		else:
			print('[' + ','.join(nbr) + ']')
