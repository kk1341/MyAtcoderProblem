#!/usr/bin/env python3
n,m,x,t,d = map(int, input().split())
if n <= m:
    print((m-n)*d + t)
elif m <= x:
    print(t-(x-m)*d)
else:
    print(t)