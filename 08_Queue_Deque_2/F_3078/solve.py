# https://derekahndev.github.io/problem%20solving/boj-3078/
from sys import stdin

# 입력
n, k = map(int, stdin.readline().rstrip().split())
# 학생 배열
students = [0] * n
# 쌍 배열
data = [0] * 21
# 정답
count = 0
# n만큼 반복
for rank in range(n):
	# 이름 입력 후 name에 이름 길이 저장
    name = len(stdin.readline().rstrip())
	# 해당 rank의 학생 위치에 이름 길이 저장
    students[rank] = name
	# 만약 rank가 K를 넘어가게 되면 범위 밖에 있는 친구의 쌍을 뺌
    if rank > k:
        data[students[rank - k - 1]] -= 1
	# 반환 값에 같은 이름 길이의 쌍 더함
    count += data[name]
	# 쌍 추가
    data[name] += 1

print(count)