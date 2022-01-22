import sys

n = int(sys.stdin.readline())
dot = []
for i in range(n):
	k = list(map(int, sys.stdin.readline().split()))
	dot.append(k)
dot = sorted(dot, key=lambda x : (x[1], x[0]))
ret = 0
for i in range(len(dot)):
	if i == 0:
		ret += abs(dot[0][0] - dot[1][0])
	elif i == len(dot) - 1:
		ret += abs(dot[i][0] - dot[i-1][0])
	else:
		if dot[i][1] == dot[i-1][1] and dot[i][1] == dot[i+1][1]:
			ret += min(abs(dot[i][0]-dot[i-1][0]), abs(dot[i][0]-dot[i+1][0]))
		elif dot[i][1] == dot[i-1][1] and dot[i][1] != dot[i+1][1]:
			ret += abs(dot[i][0] - dot[i-1][0])
		elif dot[i][1] != dot[i-1][1] and dot[i][1] == dot[i+1][1]:
			ret += abs(dot[i][0] - dot[i+1][0])
print(ret)