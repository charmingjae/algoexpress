import sys
N = int(sys.stdin.readline())

stack = []

def compare(lst):
	if lst[0] == 'push':
		stack.append(int(lst[1]))
	elif lst[0] == 'pop':
		if len(stack) == 0:
			sys.stdout.write(str(-1) + '\n')
		else:
			a = stack.pop()
			sys.stdout.write(str(a) + '\n')
	elif lst[0] == 'size':
		sys.stdout.write(str(len(stack)) + '\n')
	elif lst[0] == 'empty':
		if len(stack) == 0:
			sys.stdout.write(str(1) + '\n')
		else:
			sys.stdout.write(str(0) + '\n')
	elif lst[0] == 'top':
		if len(stack) == 0:
			sys.stdout.write(str(-1) + '\n')
		else:
			sys.stdout.write(str(stack[-1]) + '\n')
for _ in range(N):
	arr = list(map(str, sys.stdin.readline().split()))
	compare(arr)