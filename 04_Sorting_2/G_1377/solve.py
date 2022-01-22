import sys

N = int(sys.stdin.readline())

s = sorted([[int(sys.stdin.readline()), i] for i in range(N)])
dif = 0

for i in range(len(s)):
	if i != s[i][1]:
		dif = max(dif, s[i][1] - i)
print(dif + 1)
