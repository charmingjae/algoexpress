import itertools
# dictionary
dics = {}

# input
a, b, c = map(str, input().split())
a, b, c = list(a), list(b), list(c)
sets = sorted(list(set(a + b + c)))
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# init to dictionary
for i in sets:
	dics[i] = 0

numArr = []

def bind(arr):
	idx = 0
	for i in dics:
		dics[i] = arr[idx]
		idx += 1
	aNum = bNum = cNum = 0
	for i in a:
		aNum *= 10
		aNum += dics[i]
	for i in b:
		bNum *= 10
		bNum += dics[i]
	for i in c:
		cNum *= 10
		cNum += dics[i]
	if aNum + bNum == cNum:
		return 1
	else:
		return 0
for i in itertools.permutations(num, len(dics)):
	if bind(i) == 1:
		print('YES')
		exit()
print('NO')