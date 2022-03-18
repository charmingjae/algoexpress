from collections import deque
import itertools
# 입력
n = int(input())
nbrArr = deque(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈
sigInput = list(map(int, input().split()))
sigArr = deque()
for i in range(4):
	if i == 0:
		for j in range(sigInput[0]):
			sigArr.append('+')
	if i == 1:
		for j in range(sigInput[1]):
			sigArr.append('-')
	if i == 2:
		for j in range(sigInput[2]):
			sigArr.append('*')
	if i == 3:
		for j in range(sigInput[3]):
			sigArr.append('//')
# 최대, 최소 기준 값
maxNbr = -1000000001
minNbr = 1000000001

def dfs(target, idx, chk):
	global maxNbr, minNbr
	if idx == n:
		maxNbr = max(maxNbr, eval(target))
		minNbr = min(minNbr, eval(target))
		return
	if chk[0] < sigInput[0]:
		chk[0] += 1
		dfs(target + '+' + str(nbrArr[idx]), idx + 1, chk)
		chk[0] -= 1
	if chk[1] < sigInput[1]:
		chk[1] += 1
		dfs(target + '-' + str(nbrArr[idx]), idx + 1, chk)
		chk[1] -= 1
	if chk[2] < sigInput[2]:
		chk[2] += 1
		dfs(target + '*' + str(nbrArr[idx]), idx + 1, chk)
		chk[2] -= 1
	if chk[3] < sigInput[3]:
		chk[3] += 1
		dfs(target + '//' + str(nbrArr[idx]), idx + 1, chk)
		chk[3] -= 1
dfs(str(nbrArr[0]), 1, [0, 0, 0, 0])

print(maxNbr)
print(minNbr)