import sys
from collections import deque

# 카드 개수 = N, 게임 진행 횟수 = M
N, M = map(int, sys.stdin.readline().split())
# 도도 덱, 수연 덱
doDeque, suDeque = deque(), deque()
# 도도 그라운드, 수연 그라운드
doGround, suGround = deque(), deque()
# 도도 덱, 수연 덱 입력
for _ in range(N):
	doCard, suCard = map(int, sys.stdin.readline().split())
	doDeque.append(doCard)
	suDeque.append(suCard)
# 0 -> 도도, 1 -> 수연
turn = 0
printed = 0
for _ in range(M):
	# turn에 따라 도도와 수연이 카드를 그라운드에 내려놓음
	if turn == 0:
		doGround.append(doDeque.pop())
		if len(doDeque) == 0:
			sys.stdout.write('su')
			exit()
		turn = 1
	elif turn == 1:
		suGround.append(suDeque.pop())
		if len(suDeque) == 0:
			sys.stdout.write('do')
			exit()
		turn = 0
	# 수연이가 종을 울림
	if doGround and suGround and doGround[-1] + suGround[-1] == 5:
		# 도도의 그라운드를 뒤집어 수연의 데크 제일 아래에 합침
		suDeque.extendleft(doGround)
		doGround = deque()
		# 자신의 그라운드를 뒤집어 수연의 데크 제일 아래에 합침
		suDeque.extendleft(suGround)
		suGround = deque()
	# 도도가 종을 울림
	elif (doGround and doGround[-1] == 5) or (suGround and suGround[-1] == 5):
		# 도도의 그라운드를 뒤집어 수연의 데크 제일 아래에 합침
		doDeque.extendleft(suGround)
		suGround = deque()
		# 자신의 그라운드를 뒤집어 수연의 데크 제일 아래에 합침
		doDeque.extendleft(doGround)
		doGround = deque()

if printed == 0:
	if len(doDeque) > len(suDeque):
		sys.stdout.write('do')
	elif len(doDeque) < len(suDeque):
		sys.stdout.write('su')
	else:
		sys.stdout.write('dosu')