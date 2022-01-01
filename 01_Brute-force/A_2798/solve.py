import sys
import itertools
N, M = map(int, sys.stdin.readline().split())
s = []

arr = sorted(list(map(int, sys.stdin.readline().split())))
for i in list(itertools.combinations(arr, 3)):
	s.append(sum(i))
s = sorted(s)

if len(s) == 1 and s[0] <= M:
	print(s)
else:
	for i in range(len(s)):
		if s[i] > M:
			print(s[i-1])
			break
	else:
		print(s[i])