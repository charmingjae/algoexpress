s = []
n = int(input())

for i in range(n):
	x, y = map(int, input().split())
	s.append([x, y])
s = sorted(s)
for i in s:
	print(i[0], i[1])