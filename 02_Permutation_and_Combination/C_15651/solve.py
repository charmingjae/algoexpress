import sys
n, m = map(int, sys.stdin.readline().split())

s = []

def back():
	if len(s) == m:
		print(' '.join(map(str, s)))
		return
	for i in range(1, n + 1):
		s.append(i)
		back()
		s.pop()
back()