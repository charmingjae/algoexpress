n = int(input())
arr = []
for i in range(n):
	a, b = map(int, input().split())
	arr.append([a, b])
arr = sorted(arr, key=lambda x : (x[0]))
area = 0

tmp = arr
start, end, height = 0, 0, 0
detect = 0
while True:
	prev = 0
	height = 0
	tallest = max(arr, key=lambda x : x[1])
	tallest_idx = arr.index(max(arr, key=lambda x : x[1]))
	# target array 생성
	tmp = arr[0 : tallest_idx + 1]
	# arr 재조정
	if detect == 0:
		for i in tmp:
			if height < i[1]:
				end = i[0]
				area += (end - start) * height
				start, end, height = i[0], i[0] + 1, i[1]
		area += height
		start = tmp[-1][0] + 1
	elif detect != 0:
		for i in tmp:
			if height < i[1]:
				height = i[1]
				end = i[0] + 1
				area += (((end - start) * height) - prev)
				prev = (end - start) * height
	detect += 1
	start = tmp[-1][0] + 1
	arr = arr[tallest_idx + 1:]
	if len(arr) == 0:
		break
print(area)