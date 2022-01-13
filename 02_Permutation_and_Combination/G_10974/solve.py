import sys

n = int(sys.stdin.readline())
s = []

def back():
	if len(s) == n:
		print(*s)
		return
	for i in range(1, n+1):
		if i in s:
			continue
		s.append(i)
		back()
		s.pop()
back()