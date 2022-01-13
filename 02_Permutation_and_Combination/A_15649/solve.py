n, m = map(int, input().split())
arr = []
def back():
	if len(arr) == m:
		print(' '.join(list(map(str,arr))))
		return
	for i in range(1, n + 1):
		if i not in arr:
			arr.append(i)
			back()
			arr.pop()
back()