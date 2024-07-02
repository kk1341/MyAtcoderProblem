#!/usr/bin/env python3

n = int(input())
team = []

for i in range(n):
    s = input()
    win = s.count('o')
    team.append([i+1, win])

team = sorted(team, key=lambda x: x[1], reverse=True)
for i in range(n):
    print(team[i][0], end=' ')