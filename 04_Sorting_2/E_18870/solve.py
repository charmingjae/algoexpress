import sys
N = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
a = sorted(set(s))
dic = {i:v for v,i in enumerate(a)}
for i in s:
	print(dic[i], end = ' ')