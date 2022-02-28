import sys

k = int(sys.stdin.readline().rstrip())

arr = list(map(str, sys.stdin.readline().rstrip().split()))
ret = []
printed = 0
def proc(ret):
	for j in range(len(ret) - 1):
		if arr[j] == '>':
			if ret[j] < ret[j+1]:
				return 0
		elif arr[j] == '<':
			if ret[j] > ret[j+1]:
				return 0
	return 1
tar = []
def backt():
	# global printed
	if len(ret) == k + 1:
		tar.append(''.join(map(str, ret)))
		# printed = 1
		return
	# if printed == 1:
		# return
	for i in range(10):
		if i in ret:
			continue
		ret.append(i)
		if len(ret) > 1:
			if proc(ret) == 0:
				ret.pop()
				continue
		backt()
		ret.pop()
backt()
print(max(tar))
print(min(tar))