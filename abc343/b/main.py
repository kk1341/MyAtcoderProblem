#!/usr/bin/env python3
h, w, n = map(int, input().split())
filed = []
for i in range(h):
    filed.append(['.'] * w)

def run(x, y, theta):

    if theta == 360:
        theta = 0
    elif theta == -90:
        theta = 270

    if theta == 0:
        x += 1
    elif theta == 90:
        y += 1
    elif theta == 180:
        x -= 1
    elif theta == 270:
        y -= 1

x, y = 0, 0 
theta = 90
for i in range(n):
    if filed[x][y] == '.':
        filed[x][y] = '#'
        run(x, y, theta+90)
    else:
        filed[x][y] = '.'
        run(x, y, theta-90)

for i in range(h):
    print(*filed[i])