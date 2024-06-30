#!/usr/bin/env python3
n, m = map(int, input().split())
graph = []
for i in range(n+1):
    graph.append([0] * (n+1))

for i in range(m):
    u, v = map(int, input().split())
    if graph[u][v] == 0:
        graph[u][v] = 1
        graph[v][u] = 1

ans = 0
for i in range(1, n+1):
    a = []
    for j in range(1, n+1):
        if graph[i][j] == 1:
            a.append(j)
    for j in range(len(a)):
        for k in range(j+1, len(a)):
            if graph[a[j]][a[k]] == 1:
                ans += 1

print(ans//3)