# https://www.acmicpc.net/problem/14889

from itertools import combinations, permutations

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]

team_start_odds = combinations(range(N), N//2)

min_diff = 0xFFFF_FFFF_FFFF_FFFF

def getTeamStat(stats, team_comb:set):
    team_stat = 0

    for i, j in permutations(team_comb, 2):
        team_stat += stats[i][j]

    return team_stat


def getStatDiff(stats, team_comb):
    team_start = set(team_comb)
    team_link = set(range(N)) - team_start

    team_start_stat = getTeamStat(stats, team_start)
    team_link_stat = getTeamStat(stats, team_link)

    return abs(team_start_stat - team_link_stat)


for team_start in team_start_odds:
    diff = getStatDiff(stats, team_start)
    min_diff = min(diff, min_diff)

print(min_diff)
