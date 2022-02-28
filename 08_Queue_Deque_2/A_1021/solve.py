# 입력
N, M = map(int, input().split())
# 0 ~ N-1
original = [i for i in range(N)]
# 뽑을 수의 위치
locate = list(map(int, input().split()))
cnt = 0
ele = []
# 뽑아낼 숫자
for i in locate:
	ele.append(original[i-1])

def roleft(lst):
	k = lst.pop(0)
	lst.append(k)

def roright(lst):
	k = lst.pop()
	lst.insert(0, k)

# 뽑아낼 숫자 순회
for i in ele:
	# 인덱스가 0이면 패스
	if original.index(i) == 0:
		pass
	# 중간보다 좌측에 있으면 rotation left
	elif original.index(i) <= (len(original) // 2):
		for j in range(original.index(i)):
			roleft(original)
			cnt += 1
	# 중간보다 우측에 있으면 rotation right
	elif original.index(i) > (len(original) // 2):
		for j in range(len(original) - original.index(i)):
			roright(original)
			cnt += 1
	# 뽑아내기
	original.pop(0)
print(cnt)
