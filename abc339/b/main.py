#!/usr/bin/env python3
#!/usr/bin/env python3
h, w, n = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
filed = []
for i in range(h):
    filed.append(['.'] * w)

x, y, m = 0, 0, 0
for i in range(n):
    if filed[y][x] == '.':
        filed[y][x] = '#'
        m += 1
    else:
        filed[y][x] = '.'
        m += 3
    m %= 4
    x += dx[m]
    y += dy[m]
    if x < 0:
        x += w
    elif x >= w:
        x -= w
    elif y < 0:
        y += h
    elif y >= h:
        y -= h

for i in range(h):
    print(''.join(filed[i]))
        