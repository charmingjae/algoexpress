import sys
import itertools

# 짝수 N
n = int(sys.stdin.readline().rstrip())
# 선수단 목록
nbrArr = [i for i in range(n)]
# 차이를 담을 배열
retArr = []
# 팀 능력치
arr = []
# 팀 A
teamArr = []
# 팀 능력치 입력
for _ in range(n):
	arr.append(list(map(int, input().split())))

def calcTeam(tmpTeam):
	teamA, teamB = tmpTeam, list(set(nbrArr) - set(tmpTeam))
	aValue, bValue = 0, 0
	for i in list(itertools.permutations(teamA, 2)):
		aValue += arr[i[0]][i[1]]
	for i in list(itertools.permutations(teamB, 2)):
		bValue += arr[i[0]][i[1]]
	retArr.append(abs(aValue - bValue))

def backt():
	if len(teamArr) == n // 2:
		calcTeam(teamArr)
		return
	for i in range(n):
		if i in teamArr:
			continue
		teamArr.append(i)
		if teamArr != sorted(teamArr):
			teamArr.pop()
			continue
		backt()
		teamArr.pop()

backt()
print(min(retArr))