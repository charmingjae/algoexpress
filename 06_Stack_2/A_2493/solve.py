import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
tower = []
ret = []

for i in range(len(arr)):
	while len(tower) != 0:
		if tower[-1][1] < arr[i]:
			tower.pop()
		elif tower[-1][1] > arr[i]:
			ret.append(tower[-1][0] + 1)
			break
	if len(tower) == 0:
		ret.append(0)	
	tower.append([i, arr[i]])
print(*ret)