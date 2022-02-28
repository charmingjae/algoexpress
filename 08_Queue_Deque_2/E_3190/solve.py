import sys
from collections import deque

# 맵의 크기
n = int(sys.stdin.readline().rstrip())
# 뱀 처음 위치 초기화
snLoc = deque()
snLoc.append([0, 0])
snHeadRow, snHeadCol = 0, 0
# 사과 개수
appleNum = int(sys.stdin.readline().rstrip())
# 사과 위치
aplLoc = []
# 사과 위치 초기화
for _ in range(appleNum):
	a, b = map(int, sys.stdin.readline().rstrip().split())
	aplLoc.append([a - 1, b - 1])
# 명령 개수
L = int(sys.stdin.readline().rstrip())
# CP, CM, RP, RM
dir = 'CP'
cnt = 0
command = []
# 명령 입력받기
for _ in range(L):
	a, b = map(str, sys.stdin.readline().rstrip().split())
	a = int(a)
	command.append([a, b])
untilA, untilB = 0, ''
for i in command:
	# 명령 입력
	untilA, untilB = i[0], i[1]
	# a 전까지 직진
	while cnt < int(untilA):
		cnt += 1
		if dir == 'CP':
			if [snHeadRow, snHeadCol + 1] in aplLoc:
				aplLoc.pop(aplLoc.index([snHeadRow, snHeadCol + 1]))
				snLoc.append([snHeadRow, snHeadCol + 1])
				snHeadCol += 1
			else:
				if [snHeadRow, snHeadCol + 1] in snLoc or snHeadCol + 1 >= n:
					print(cnt)
					exit()
				snLoc.popleft()
				snLoc.append([snHeadRow, snHeadCol + 1])
				snHeadCol += 1
		elif dir == 'CM':
			if [snHeadRow, snHeadCol - 1] in aplLoc:
				aplLoc.pop(aplLoc.index([snHeadRow, snHeadCol - 1]))
				snLoc.append([snHeadRow, snHeadCol - 1])
				snHeadCol -= 1
			else:
				if [snHeadRow, snHeadCol - 1] in snLoc or snHeadCol - 1 < 0:
					print(cnt)
					exit()
				snLoc.popleft()
				snLoc.append([snHeadRow, snHeadCol - 1])
				snHeadCol -= 1
		elif dir == 'RP':
			if [snHeadRow + 1, snHeadCol] in aplLoc:
				aplLoc.pop(aplLoc.index([snHeadRow + 1, snHeadCol]))
				snLoc.append([snHeadRow + 1, snHeadCol])
				snHeadRow += 1
			else:
				if [snHeadRow + 1, snHeadCol] in snLoc or snHeadRow + 1 >= n:
					print(cnt)
					exit()
				snLoc.popleft()
				snLoc.append([snHeadRow + 1, snHeadCol])
				snHeadRow += 1
		elif dir == 'RM':
			if [snHeadRow - 1, snHeadCol] in aplLoc:
				aplLoc.pop(aplLoc.index([snHeadRow - 1, snHeadCol]))
				snLoc.append([snHeadRow - 1, snHeadCol])
				snHeadRow -= 1
			else:
				if [snHeadRow - 1, snHeadCol] in snLoc or snHeadRow - 1 < 0:
					print(cnt)
					exit()
				snLoc.popleft()
				snLoc.append([snHeadRow - 1, snHeadCol])
				snHeadRow -= 1
		# print('prev direction : ', dir)
		# print('sn body : ', snLoc)
		# print('apl : ', aplLoc)
		# print('cnt : ', cnt)
		# print()
	if dir == 'CP':
		if untilB == 'L':
			dir = 'RM'
		elif untilB == 'D':
			dir = 'RP'
	elif dir == 'CM':
		if untilB == 'L':
			dir = 'RP'
		elif untilB == 'D':
			dir = 'RM'
	elif dir == 'RP':
		if untilB == 'L':
			dir = 'CP'
		elif untilB == 'D':
			dir = 'CM'
	elif dir == 'RM':
		if untilB == 'L':
			dir = 'CM'
		elif untilB == 'D':
			dir = 'CP'
	# print('after direction : ', dir)

while True:
		cnt += 1
		if dir == 'CP':
			if [snHeadRow, snHeadCol + 1] in aplLoc:
				aplLoc.pop(aplLoc.index([snHeadRow, snHeadCol + 1]))
				snLoc.append([snHeadRow, snHeadCol + 1])
				snHeadCol += 1
			else:
				if [snHeadRow, snHeadCol + 1] in snLoc or snHeadCol + 1 >= n:
					print(cnt)
					exit()
				snLoc.popleft()
				snLoc.append([snHeadRow, snHeadCol + 1])
				snHeadCol += 1
		elif dir == 'CM':
			if [snHeadRow, snHeadCol - 1] in aplLoc:
				aplLoc.pop(aplLoc.index([snHeadRow, snHeadCol - 1]))
				snLoc.append([snHeadRow, snHeadCol - 1])
				snHeadCol -= 1
			else:
				if [snHeadRow, snHeadCol - 1] in snLoc or snHeadCol - 1 < 0:
					print(cnt)
					exit()
				snLoc.popleft()
				snLoc.append([snHeadRow, snHeadCol - 1])
				snHeadCol -= 1
		elif dir == 'RP':
			if [snHeadRow + 1, snHeadCol] in aplLoc:
				aplLoc.pop(aplLoc.index([snHeadRow + 1, snHeadCol]))
				snLoc.append([snHeadRow + 1, snHeadCol])
				snHeadRow += 1
			else:
				if [snHeadRow + 1, snHeadCol] in snLoc or snHeadRow + 1 >= n:
					print(cnt)
					exit()
				snLoc.popleft()
				snLoc.append([snHeadRow + 1, snHeadCol])
				snHeadRow += 1
		elif dir == 'RM':
			if [snHeadRow - 1, snHeadCol] in aplLoc:
				aplLoc.pop(aplLoc.index([snHeadRow - 1, snHeadCol]))
				snLoc.append([snHeadRow - 1, snHeadCol])
				snHeadRow -= 1
			else:
				if [snHeadRow - 1, snHeadCol] in snLoc or snHeadRow - 1 < 0:
					print(cnt)
					exit()
				snLoc.popleft()
				snLoc.append([snHeadRow - 1, snHeadCol])
				snHeadRow -= 1
		# print('prev direction : ', dir)
		# print('sn body : ', snLoc)
		# print('apl : ', aplLoc)
		# print()