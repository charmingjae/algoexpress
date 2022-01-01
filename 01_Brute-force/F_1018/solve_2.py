n, m = map(int, input().split())
solve = []
arr = []

for _ in range(n):
	arr.append(list(input()))

for r in range(n - 7):
	for c in range(m - 7):
		a = 0
		b = 0
		for i in range(r, r + 8):
			for j in range(c, c + 8):
				if (i + j)%2 == 0:
					if arr[i][j] != 'B':
						a += 1
					elif arr[i][j] != 'W':
						b += 1
				else:
					if arr[i][j] != 'B':
						b += 1
					elif arr[i][j] != 'W':
						a += 1
		solve.append(a)
		solve.append(b)
print(min(solve))