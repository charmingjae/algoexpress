n = int(input())
s = []
for i in range(n):
	a = []
	k = list(input().split())
	a.append(k[0])
	a.append(int(k[1]))
	a.append(int(k[2]))
	a.append(int(k[3]))
	s.append(a)
s = sorted(s, key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in s:
	print(i[0])