import sys
N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
ret = 1
for i in arr:
	if ret >= i:
		ret += i
	else:
		break
print(ret)