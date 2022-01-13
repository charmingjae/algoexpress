n = int(input())
cnt = 0
def ishan(a):
	s = -1
	arr = list(map(int, list(str(a))))
	if len(arr) == 1:
		return 1
	s = arr[0] - arr[1]
	for i in range(len(arr) - 1):
		if arr[i] - arr[i+1] != s:
			return 0
	return 1

for i in range(1, n+1):
	if ishan(i) == 1:
		cnt += 1
print(cnt)