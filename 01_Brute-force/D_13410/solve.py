n, k = map(int, input().split())
s = []
for i in range(k):
	k = int(''.join(list(reversed(str(n * (i + 1))))))
	s.append(k)
print(max(s))