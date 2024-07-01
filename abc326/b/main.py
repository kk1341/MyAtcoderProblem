#!/usr/bin/env python3

n = int(input())
while n < 1000:
    m = list(str(n))
    if int(m[0]) * int(m[1]) == int(m[2]):
        print(n)
        exit()
    n += 1