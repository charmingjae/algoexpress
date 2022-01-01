n, m = map(int, input().split())
solve = []
arr = []
tmp = []
for _ in range(n):
	arr.append(list(input()))

def getdif(arr1, arr2):
	cnt = 0
	for i in range(8):
		for j in range(8):
			if arr1[i][j] != arr2[i][j]:
				cnt += 1
	return cnt

type1 = [['W','B','W','B','W','B','W','B'],
		['B','W','B','W','B','W','B','W'],
		['W','B','W','B','W','B','W','B'],
		['B','W','B','W','B','W','B','W'],
		['W','B','W','B','W','B','W','B'],
		['B','W','B','W','B','W','B','W'],
		['W','B','W','B','W','B','W','B'],
		['B','W','B','W','B','W','B','W']]

type2 = [['B','W','B','W','B','W','B','W'],
		['W','B','W','B','W','B','W','B'],
		['B','W','B','W','B','W','B','W'],
		['W','B','W','B','W','B','W','B'],
		['B','W','B','W','B','W','B','W'],
		['W','B','W','B','W','B','W','B'],
		['B','W','B','W','B','W','B','W'],
		['W','B','W','B','W','B','W','B']]

for r in range(n - 7):
	for c in range(m - 7):
		target = arr[r][c]
		tmp = []
		for i in range(r, r + 8):
			box = []
			for j in range(c, c + 8):
				box.append(arr[i][j])
			tmp.append(box)
		solve.append(getdif(type2, tmp))
		solve.append(getdif(type1, tmp))
print(min(solve))