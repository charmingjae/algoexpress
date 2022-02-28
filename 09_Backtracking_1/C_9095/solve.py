n = int(input())

target = []
usage = [1, 2, 3]
for _ in range(n):
	target.append(int(input()))
sumPerNbr = []
cnt = 0

def backt(tar):
	global cnt
	if len(sumPerNbr) > tar:
		return
	if sum(sumPerNbr) == tar:
		cnt += 1
		return
	for i in usage:
		sumPerNbr.append(i)
		backt(tar)
		sumPerNbr.pop()

for i in target:
	backt(i)
	print(cnt)
	cnt = 0
	sumPerNbr = []