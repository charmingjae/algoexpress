import sys

n = int(sys.stdin.readline())
arr = [0] * 10001
for i in range(n):
	arr[int(sys.stdin.readline())] += 1
for i in range(10001):
	for j in range(arr[i]):
		sys.stdout.write(str(i)+'\n')