from collections import deque
import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque()

def len1(command):
	global arr
	if command == 'pop':
		if arr:
			sys.stdout.write(str(arr.popleft()) + '\n')
		else:
			sys.stdout.write(str(-1) + '\n')
	elif command == 'size':
		sys.stdout.write(str(len(arr)) + '\n')
	elif command == 'empty':
		if arr:
			sys.stdout.write(str(0) + '\n')
		else:
			sys.stdout.write(str(1) + '\n')
	elif command == 'front':
		if arr:
			sys.stdout.write(str(arr[0]) + '\n')
		else:
			sys.stdout.write(str(-1) + '\n')
	elif command == 'back':
		if arr:
			sys.stdout.write(str(arr[-1]) + '\n')
		else:
			sys.stdout.write(str(-1) + '\n')

def len2(arrs):
	global arr
	if arrs[0] == 'push':
		arr.append(arrs[1])

for _ in range(n):
	command = list(sys.stdin.readline().rstrip().split())
	if len(command) == 1:
		len1(command[0])
	elif len(command) == 2:
		len2(command)