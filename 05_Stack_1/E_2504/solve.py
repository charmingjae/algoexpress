n = list(input())
stack = []
err = 0

for i in n:
	# 무조건 append 해야 하는 경우
	if i == '(' or i == '[':
		stack.append(i)
	# ')'를 만났을 때 -> '('를 만날 때까지 아래 실행
	elif i == ')':
		if len(stack) == 0:
			print(0)
			exit(0)
		total = 0
		while len(stack) > 0:
			target = stack.pop()
			if target == '[':
				print(0)
				exit(0)
			elif target == '(':
				if total == 0:
					stack.append(2)
				else:
					stack.append(total * 2)
				break
			else:
				total += target
	elif i == ']':
		if len(stack) == 0:
			print(0)
			exit(0)
		total = 0
		while len(stack) > 0:
			target = stack.pop()
			if target == '(':
				print(0)
				exit(0)
			elif target == '[':
				if total == 0:
					stack.append(3)
				else:
					stack.append(total * 3)
				break
			else:
				total += target

for i in stack:
	if i == '(' or i == '[' or i == ']' or i == ')':
		print(0)
		exit(0)
if err != 1:
	print(sum(stack))