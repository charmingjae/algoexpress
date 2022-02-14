# https://kimmeh1.tistory.com/344
n = int(input())
s = list(input())
stack = []
counter = [0] * n
ret = 0
cnt = 0
for i in range(n):
	if s[i] == '(':
		stack.append(i)
	elif s[i] == ')':
		if len(stack) != 0:
			counter[i] = counter[stack[-1]] = 1
			stack.pop()

for i in range(n):
	if counter[i] == 1:
		cnt += 1
		ret = max(ret, cnt)
	else:
		cnt = 0
print(ret)