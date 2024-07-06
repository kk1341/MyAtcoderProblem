#!/usr/bin/env python3
a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

x1_min, x1_max = min(a, d), max(a, d)
y1_min, y1_max = min(b, e), max(b, e)
z1_min, z1_max = min(c, f), max(c, f)

x2_min, x2_max = min(g, j), max(g, j)
y2_min, y2_max = min(h, k), max(h, k)
z2_min, z2_max = min(i, l), max(i, l)

if x1_min < x2_max and x2_min < x1_max and y1_min < y2_max and y2_min < y1_max and z1_min < z2_max and z2_min < z1_max :
    print('Yes')
else:
    print('No')