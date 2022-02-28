l, c = map(int, input().split())

arr = sorted(list(map(str, input().split())))
vowels = ['a', 'e', 'i', 'o', 'u']
ret = []

def isRight(arr):
	vow = 0
	con = 0
	for i in arr:
		if i in vowels:
			vow += 1
		else:
			con += 1
	if vow >= 1 and con >= 2:
		return 1
	else:
		return 0

def backt():
	if len(ret) == l:
		if isRight(ret):
			print(''.join(ret))
		return
	for i in arr:
		if i in ret:
			continue
		ret.append(i)
		if ret != sorted(ret):
			ret.pop()
			continue
		backt()
		ret.pop()

backt()