import itertools
n = sorted(list(map(int, input())), reverse = True)
if sum(n) % 3 == 0:
	if n[-1] == 0:
		print(''.join(map(str,n)))
	else:
		print(-1)
else:
	print(-1)