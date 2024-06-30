#!/usr/bin/env python3
n = int(input())
A = list(map(int, input().split()))
ball = []

for a in A:

    ball.append(a)
    while True:
        if len(ball) <= 1 or ball[-1] != ball[-2]:
            break
        
        ball.pop()
        ball[-1] += 1

print(len(ball))