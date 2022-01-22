import sys

T = int(sys.stdin.readline())
for i in range(T):
	N, M = map(int, sys.stdin.readline().split())
	A = sorted(map(int, sys.stdin.readline().split()), reverse = True)
	B = sorted(map(int, sys.stdin.readline().split()), reverse = True)
	ret = 0
	for i in A:
		cnt = 0
		for j in B:
			if i > j:
				ret += len(B) - cnt
				break
			else:
				cnt += 1
	print(ret)