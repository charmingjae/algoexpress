import sys

N = int(sys.stdin.readline().rstrip())

schedule = []
for _ in range(N):
	T, P = map(int, sys.stdin.readline().rstrip().split())
	schedule.append([T, P])

pm = 0
pay = 0
def backt(day):
	global pay
	global pm
	if day >= N:
		return
	while day < N:
		if day + 1 + schedule[day][0] <= N + 1:
			pay += schedule[day][1]
			pm = max(pm, pay)
			backt(day + schedule[day][0])
			pay -= schedule[day][1]
		day += 1

backt(0)
print(pm)