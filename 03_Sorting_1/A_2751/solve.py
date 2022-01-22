arr = []
n = int(input())
for i in range(n):
	arr.append(int(input()))
arr = sorted(arr)
print('\n'.join(map(str,arr)))