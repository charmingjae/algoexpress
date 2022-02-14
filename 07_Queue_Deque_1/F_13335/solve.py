import sys

# 입력
N, W, L = map(int, sys.stdin.readline().split())
car = list(map(int, sys.stdin.readline().split()))

# 다리에 올라갈 수 있는 트럭 용량 초기화
bridge = [0 for _ in range(W)]
# 걸리는 시간
time = 0

while True:
	# 대기 중인 차가 있을 때
	if car:
		# 현재 다리 위에 올라가 있는 차들의 무게 + 다음에 올라올 차량의 무게가 다리가 버틸 수 있는 무게 범위 내에 있을 때
		if sum(bridge) + car[0] >= 0 and sum(bridge) + car[0] <= L:
			# 맨 앞에 있는 요소를 제거
			bridge.pop(0)
			# 맨 뒤에 대기 중인 차 중 맨 앞에 있는 차량을 다리 위에 올림
			bridge.append(car.pop(0))
			# 시간 증가
			time += 1
		# 무게가 넘을 때
		elif sum(bridge) + car[0] > L:
			# 맨 앞에 있는 요소 제거
			bridge.pop(0)
			# 제거 했을 때 정상 범위 안에 들어온다면 대기 중인 차 중 맨 앞에 있는 차량을 다리 위에 올림
			if sum(bridge) + car[0] >= 0 and sum(bridge) + car[0] <= L:
				bridge.append(car.pop(0))
			# 범위 밖이라면
			else:
				# 0 넣기
				bridge.append(0)
			# 시간 증가
			time += 1
	# 대기 중인 차가 없을 때
	else:
		# 모든 차량이 다리에서 나올 수 있도록 맨 앞에 있는 요소 제거 후 뒤에 0 집어넣음
		if sum(bridge) > 0:
			while sum(bridge) > 0:
				bridge.pop(0)
				bridge.append(0)
				time += 1
		sys.stdout.write(str(time) + '\n')
		break