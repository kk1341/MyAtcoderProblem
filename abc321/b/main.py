#!/usr/bin/env python3
n, x = map(int, input().split())
A = list(map(int, input().split()))

for last_score in range(0, 101):
    all_score = A + [last_score]
    all_score.sort()
    all_score.pop(0)
    all_score.pop(-1)
    if sum(all_score) >= x:
        print(last_score)
        exit()

print(-1)