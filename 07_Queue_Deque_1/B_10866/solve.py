import sys
n = int(sys.stdin.readline())

que = []

def command_len_1(command):
	global que
	if command == 'pop_front':
		if que:
			a = que.pop(0)
			sys.stdout.write(a + '\n')
		else:
			sys.stdout.write(str(-1) + '\n')
	elif command == 'pop_back':
		if que:
			a = que.pop()
			sys.stdout.write(a + '\n')
		else:
			sys.stdout.write(str(-1) + '\n')
	elif command == 'size':
		sys.stdout.write(str(len(que)) + '\n')
	elif command == 'empty':
		if que:
			sys.stdout.write(str(0) + '\n')
		else:
			sys.stdout.write(str(1) + '\n')
	elif command == 'front':
		if que:
			sys.stdout.write(str(que[0]) + '\n')
		else:
			sys.stdout.write(str(-1) + '\n')
	elif command == 'back':
		if que:
			sys.stdout.write(str(que[-1]) + '\n')
		else:
			sys.stdout.write(str(-1) + '\n')

def command_len_2(command, arg):
	global que
	if command == 'push_front':
		que.insert(0, arg)
	elif command == 'push_back':
		que.append(arg)

for _ in range(n):
	command = sys.stdin.readline().rstrip().split()
	if len(command) == 1:
		command_len_1(command[0])
	elif len(command) == 2:
		command_len_2(command[0], command[1])