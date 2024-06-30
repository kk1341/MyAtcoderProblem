#!/usr/bin/env python3
n = int(input())
A = list(map(int, input().split()))
player = []

for i in range(len(A)):
    player.append(0)
    player = [A[i]+x for x in player]

ans = 0
for i in range(len(A)):
    if player[i] > 3:
        ans += 1

print(ans)