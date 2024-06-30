#!/usr/bin/env python3
h, w = map(int, input().split())
koma = []
for i in range(h):
    S = input()
    for j in range(w):
        if S[j] == 'o':
            koma.append([i, j])

print(abs(koma[0][0] - koma[1][0]) + abs(koma[0][1] - koma[1][1]))