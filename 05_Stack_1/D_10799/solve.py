N = list(input())
tmp = []
cnt = 0
for i in range(len(N)):
	if i == 0:
		if N[i] == ')':
			print(0)
			break
		else:
			tmp.append(N[i])
	else:
		if N[i] == '(':
			tmp.append(N[i])
		else:
			if N[i-1] == '(':
				tmp.pop()
				cnt += len(tmp)
			else:
				tmp.pop()
				cnt += 1
print(cnt)