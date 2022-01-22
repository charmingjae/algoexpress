T = int(input())

for i in range(T):
	N, K, MINE, M = map(int, input().split())
	# score, total, input count, last input
	arr = [[[0 for _ in range(K + 1)], 0, 0, 0, i] for i in range(N + 1)]
	for idx in range(M):
		team, target, score = map(int, input().split())
		arr[team][0][target] = max(arr[team][0][target], score)
		arr[team][1] = sum(arr[team][0])
		arr[team][2] += 1
		arr[team][3] = idx
	arr = sorted(arr, key=lambda x : (-x[1], x[2], x[3]))
	for i in range(len(arr)):
		if arr[i][4] == MINE:
			print(i+1)
			break