from collections import deque
import sys

n, k, m = map(int, sys.stdin.readline().split())
arr = deque(range(1, n+1))
i = 0
flag = 0
while arr:
	if flag == 0:
		for _ in range(k-1):
			arr.append(arr.popleft())
	elif flag == 1:
		for _ in range(k):
			arr.appendleft(arr.pop())
	i += 1
	sys.stdout.write(str(arr.popleft()) + '\n')
	if i == m:
		flag = 1 - flag
		i = 0