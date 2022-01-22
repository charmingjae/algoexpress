import sys
T = int(sys.stdin.readline())
for i in range(T):
	N = int(sys.stdin.readline())
	memo1 = set(map(int, sys.stdin.readline().split()))
	N = int(sys.stdin.readline())
	memo2 = list(map(int, sys.stdin.readline().split()))
	for i in memo2:
		if i in memo1:
			sys.stdout.write(str(1) + '\n')
		else:
			sys.stdout.write(str(0) + '\n')