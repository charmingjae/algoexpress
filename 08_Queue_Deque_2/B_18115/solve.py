import sys
from collections import deque

# 입력
N = int(sys.stdin.readline())
A = list(reversed(list(map(int, sys.stdin.readline().rstrip().split()))))
# 원본이 저장될 곳
ret = deque()
# 1 -> 2 -> 3 -> 4 -> 5 ...
target_card = 1
for i in A:
	if i == 1:
		ret.appendleft(target_card)
	elif i == 2:
		ret.insert(1, target_card)
	elif i == 3:
		ret.append(target_card)
	target_card += 1
print(*ret)