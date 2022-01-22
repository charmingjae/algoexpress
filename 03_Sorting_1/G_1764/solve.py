import sys
n, m = map(int, sys.stdin.readline().split())
b = set()
d = set()
cnt = 0

for i in range(n):
	d.add(sys.stdin.readline().rstrip())
for i in range(m):
	b.add(sys.stdin.readline().rstrip())
tmp = sorted(b&d)

print(len(tmp))
print('\n'.join(tmp))