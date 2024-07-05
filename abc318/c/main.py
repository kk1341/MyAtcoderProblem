#!/usr/bin/env python3
n, d, p = map(int, input().split())
F = sorted(list(map(int, input().split())), reverse=True)

A = []
index = 0
while True:
    if p < sum(F[index:index+d]):
        A.append(p)
    else:
        A += F[index:]
        break

    index += d

print(sum(A))    