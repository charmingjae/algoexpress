import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
is_printed = 0
for i in range(n-1, 0, -1):
	if arr[i-1] > arr[i]:
		for j in range(n-1, 0, -1):
			if arr[i-1] > arr[j]:
				arr[i-1], arr[j] = arr[j], arr[i-1]
				arr = arr[:i] + list(reversed(arr[i:]))
				print(*arr)
				is_printed = 1
				break
	if is_printed ==1:
		break
if is_printed == 0:
	print(-1)
