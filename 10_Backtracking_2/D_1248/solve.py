import itertools

# input
n = int(input())
signArr = list(input())

# nbr arr
allNbr = [i for i in range(-10, 11)]
parseSignArr = []
# parse signArr
for i in range(n):
	tmp = [0] * i
	for j in range(n - i):
		tmp.append(signArr.pop(0))
	parseSignArr.append(tmp)

ret = []
def checkSum(idx):
	hap = 0
	for i in range(idx, -1, -1):
		hap += ret[i]
		if parseSignArr[i][idx] == '+' and hap <= 0:
			return 0
		elif parseSignArr[i][idx] == '-' and hap >= 0:
			return 0
		elif parseSignArr[i][idx] == '0' and hap != 0:
			return 0
	return 1

ret = []
def backt(idx):
	if idx == n:
		print(*ret)
		exit()
	for i in range(-10, 11):
		ret.append(i)
		if checkSum(idx):
			backt(idx + 1)
		ret.pop()

backt(0)