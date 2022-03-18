# 입력
k, n, f = map(int, input().split())
# 친구 짝지어주기
grp = {}
for i in range(n):
	grp[i+1] = list()
for i in range(f):
	a, b = map(int, input().split())
	if a not in grp[b]:
		grp[b].append(a)
	if b not in grp[a]:
		grp[a].append(b)

friend = []
isPrinted = 0
def backt():
	global isPrinted
	if isPrinted == 1:
		return
	if len(friend) == k:
		for people in friend:
			print(people)
		exit()
		isPrinted = 1
		return
	for i in range(1, n+1):
		flg = 0
		if i in friend:
			continue
		for j in friend:
			if i not in grp[j]:
				flg = 1
				break
		if flg == 1:
			continue
		friend.append(i)
		if friend != sorted(friend):
			friend.pop()
			continue
		backt()
		friend.pop()

backt()
print(-1)