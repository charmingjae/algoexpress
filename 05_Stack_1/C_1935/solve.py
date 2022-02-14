alpha = 'ABCDEFGHIJKLMNOPQURSTUVWXYZ'
nums = []
alpha_idx = 0

n = int(input())
magnum = list(input())
for i in range(n):
	nums.append(int(input()))

tmp = []
for i in magnum:
	if i in alpha:
		tmp.append(nums[ord(i) - ord('A')])
	else:
		b = tmp.pop()
		a = tmp.pop()
		if i == '+':
			tmp.append(a + b)
		elif i == '-':
			tmp.append(a - b)
		elif i == '*':
			tmp.append(a * b)
		elif i == '/':
			tmp.append(a / b)
print(f"{tmp[0]:.2f}")