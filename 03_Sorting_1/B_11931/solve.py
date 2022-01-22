arr = []
n = int(input())
for i in range(n):
	arr.append(int(input()))
arr = sorted(arr, reverse=True)
print('\n'.join(map(str,arr)))