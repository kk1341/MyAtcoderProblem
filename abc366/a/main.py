#!/usr/bin/env python3
n, t, a = map(int, input().split())
still = n - (t+a)
if t > a:
    if t > a + still:
        print('Yes')
    else:
        print('No')
else:
    if a > t + still:
        print('Yes')
    else:
        print('No')
