N = int(input())

for i in range(N + 1):
	a = i + sum(list(map(int, list(str(i)))))
	if a == N:
		print(i)
		break
else:
	print(0)