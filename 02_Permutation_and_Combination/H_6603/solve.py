s = []
def backt(lst):
	if len(s) == 6:
		print(*s)
		return
	for i in lst:
		if i in s:
			continue
		s.append(i)
		if s != sorted(s):
			s.pop()
			continue
		backt(lst)
		s.pop()
	

while True:
	arr = list(map(int, input().split()))
	if len(arr) == 1 and arr[0] == 0:
		break
	lst = arr[1:]
	backt(lst)
	print()