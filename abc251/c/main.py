#!/usr/bin/env python3
n = int(input())
S, T = [], []
for i in range(n):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

best = -1
best_score = -1

appeared = set()
for i in range(n):
    if S[i] in appeared:
        continue
    appeared.add(S[i])
    if best_score < T[i]:
        best_score = T[i]
        best = i+1

print(best)