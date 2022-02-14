import sys
que = []

def command(strs):
	global que
	if strs == 'front':
		if que:
			sys.stdout.write(que[0]+'\n')
		else:
			sys.stdout.write(str(-1) + '\n')
	elif strs == 'pop':
		if que:
			a = que.pop(0)
			sys.stdout.write(a + '\n')
		else:
			sys.stdout.write(str(-1) + '\n')
	elif strs == 'size':
		print(len(que))
	elif strs == 'empty':
		if que:
			sys.stdout.write(str(0)+'\n')
		else:
			sys.stdout.write(str(1)+'\n')
	elif strs == 'back':
		if que:
			sys.stdout.write(que[-1] + '\n')
		else:
			sys.stdout.write(str(-1)+'\n')

def pushs(command, arg):
	global que
	if command == 'push':
		que.append(arg)

n = int(sys.stdin.readline())

for _ in range(n):
	commands = list(sys.stdin.readline().rstrip().split())
	if len(commands) == 2:
		pushs(commands[0], commands[1])
	elif len(commands) == 1:
		command(commands[0])