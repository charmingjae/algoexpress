import sys

t = int(sys.stdin.readline())

for k in range(t):
	# 문서 개수, 궁금한 문서의 위치
	n, m = map(int, sys.stdin.readline().split())
	# 임시 입력
	tmp = list(map(int, sys.stdin.readline().split()))
	# 중요도 배열
	imp = []
	# 임시 배열에서 중요도와 인덱스 옮기기
	for i in range(len(tmp)):
		imp.append([tmp[i], i])
	target_comp, target_idx = imp[m][0], imp[m][1]
	cnt = 0
	while True:
		if len(list(set(tmp))) == 1:
			highOne = imp[0][0]
		else:
			highOne = sorted(imp, key=lambda x : (x[0], x[1]), reverse=True)[0][0]
		if imp[0][0] == highOne:
			a = imp.pop(0)
			cnt += 1
			if len(list(set(tmp))) == 1:
				tmp.pop(0)
			else:
				tmp.pop(tmp.index(a[0]))
			if a[0] == target_comp and a[1] == target_idx:
				print(cnt)
				break
		else:
			a = imp.pop(0)
			imp.append(a)