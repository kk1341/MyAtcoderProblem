#!/usr/bin/env python3

n, m = map(int, input().split())
a = list(map(int, input().split()))
A = []
for i in range(m):
    A.append([a[i], i])
player = [0] * n
already_solve_problem = []

max_score = 0
for i in range(n):
    s = input()
    player_solve_problem = []
    for j in range(m):
        if s[j] == 'o':
            player[i] += A[j][0]
            player_solve_problem.append(1)
        else:
            player_solve_problem.append(0)

    player[i] += (i+1)
    already_solve_problem.append(player_solve_problem)
    max_score = max(player[i], max_score)

A = sorted(A, key=lambda x: x[0], reverse=True)
for i in range(n):
    add_solve_problem = 0
    for j in range(m):
        if player[i] < max_score and already_solve_problem[i][A[j][1]] == 0 :
            player[i] += A[j][0]
            add_solve_problem += 1
        elif already_solve_problem[i][A[j][1]] == 1:
            continue
        else:
            break
    print(add_solve_problem)