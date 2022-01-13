import sys

r, b = map(int, sys.stdin.readline().split())
area = r + b
l, w = 0, 0
while True:
	# w += 1 할 경우 고려해보기
	l += 1
	w = area // l
	if l * w == area and (l + w) * 2 - 4 == r and l >= w:
		print(l, w)
		break