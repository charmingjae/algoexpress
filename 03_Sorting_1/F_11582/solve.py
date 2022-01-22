n = int(input())
arr = list(map(int, input().split()))
lvl = int(input())

def dosort(arr1, arr2):
	tmp = []
	for i in arr1:
		tmp.append(i)
	for j in arr2:
		tmp.append(j)
	return sorted(tmp)

k = []
for i in range(0, len(arr)-1, 2):
	s = []
	s.append(arr[i])
	s.append(arr[i+1])
	k.append(s)
for i in range(len(k)):
	k[i] = sorted(k[i])

human = n // 2

while human > lvl:
	m = []
	for i in range(0, len(k)-1, 2):
		m.append(dosort(k[i], k[i+1]))
	k = m
	human = human // 2

m = []
for i in k:
	for j in i:
		m.append(j)
print(*m)