import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
nbr = list(map(int, input().rstrip()))

tmp = []
remain = k

for i in range(n):
	while remain > 0 and tmp:
		if tmp[-1] < nbr[i]:
			tmp.pop()
			remain -= 1
		else:
			break
	tmp.append(nbr[i])
for i in range(n-k):
	print(tmp[i], end='')