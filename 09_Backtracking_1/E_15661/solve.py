import itertools

n = int(input())
# team score input
arr = [list(map(int, input().split())) for _ in range(n)]
# member
member = [i+1 for i in range(n)]
# collect score
ret = []
team = []
mins = 99999999

def backt():
	global mins
	if len(team) > 1:
		teamA, teamB = team, list(set(member) - set(team))
		scrTeamA, scrTeamB = 0, 0
		for i in list(itertools.combinations(teamA, 2)):
			scrTeamA += arr[i[0] - 1][i[1] - 1] + arr[i[1] - 1][i[0] - 1]
		for i in list(itertools.combinations(teamB, 2)):
			scrTeamB += arr[i[0] - 1][i[1] - 1] + arr[i[1] - 1][i[0] - 1]
		mins = min(mins, abs(scrTeamA - scrTeamB))
	for i in member:
		if i in team:
			continue
		team.append(i)
		if team != sorted(team) or len(team) > n // 2:
			team.pop()
			continue
		backt()
		team.pop()

backt()
print(mins)