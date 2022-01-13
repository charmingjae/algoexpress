import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

x = 0
y = 0
find = 0
for i in range(n-1, 0, -1):
	if arr[i-1] < arr[i]:
		for j in range(n-1, 0, -1):
			if arr[i-1] < arr[j]:
				arr[i-1], arr[j] = arr[j], arr[i-1]
				arr = arr[:i] + sorted(arr[i:])
				print(*arr)
				find = 1
				break
	if find == 1:
		break
if find == 0:
	print(-1)