import sys

input = sys.stdin.readline
print = sys.stdout.write

a = input().rstrip()
b = input().rstrip()
bomb_len = len(b)
stack = []

for i in a:
	stack.append(i)
	if ''.join(stack[-bomb_len:]) == b:
		for _ in range(bomb_len):
			stack.pop()

if stack:
	for i in stack:
		print(i)
else:
	print('FRULA')
