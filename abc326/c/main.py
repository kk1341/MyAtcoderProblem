#!/usr/bin/env python3
import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(n):
    prezent = bisect.bisect_left(A, A[i]+m) - i
    ans = max(ans, prezent)

print(ans)