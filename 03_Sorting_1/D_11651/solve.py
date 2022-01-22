s = []
n = int(input())

for i in range(n):
	x, y = map(int, input().split())
	s.append([x, y])
s = sorted(s, key=lambda x : (x[1], x[0]))
for i in s:
	print(i[0], i[1])