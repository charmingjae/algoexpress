n = int(input())
arr = []
rnk = [1 for _ in range(n)]

for _ in range(n):
	arr.append(list(map(int, input().split())))

for i in range(len(arr)):
	for j in range(len(arr)):
		if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
			rnk[j] += 1
print(' '.join(list(map(str, rnk))))