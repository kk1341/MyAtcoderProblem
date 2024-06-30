#!/usr/bin/env python3
n, a, b = map(int, input().split())

def swap(mas1, mas2):
    tmp = mas1
    mas1 = mas2
    mas2 = tmp
    return mas1, mas2

mas1 = '.'
mas2 = '#'
for i in range(1, a*n+1):
    ans = ''
    for j in range(1, n+1):
        if j % 2 != 0:
            ans += mas1 * b
        else:
            ans += mas2 * b
    print(ans)
    if i % a == 0:
        mas1, mas2 = swap(mas1, mas2)