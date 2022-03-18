# input map
arr = [list(map(int, input().split())) for i in range(9)]
# 현재 0인 row, column 위치
zeroArr = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
# flag
isPrinted = 0

def isPromising(i, j):
	promised = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	for idx in range(9):
		if arr[idx][j] in promised:
			promised.remove(arr[idx][j])
		if arr[i][idx] in promised:
			promised.remove(arr[i][idx])
	
	cellX, cellY = i//3, j//3
	for p in range(cellX * 3 , (cellX + 1) * 3):
		for q in range(cellY * 3 , (cellY + 1) * 3):
			if arr[p][q] in promised:
				promised.remove(arr[p][q])
	return promised


def backt(location):
	global isPrinted
	# 출력 되었으면 리턴
	if isPrinted == 1:
		return
	# 0 타겟 위치가 zeroArr의 길이보다 같다면 = 모든 zero 위치를 다 채웠으면 출력
	if location == len(zeroArr):
		for i in arr:
			print(*i)
		isPrinted = 1
		return
	(i, j) = zeroArr[location]
	promiseArr = isPromising(i, j)
	for k in promiseArr:
		arr[i][j] = k
		backt(location + 1)
		arr[i][j] = 0

backt(0)