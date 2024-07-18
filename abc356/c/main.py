#!/usr/bin/env python3
n, m, k = map(int, input().split())
C, A, R = [], [], []
for _ in range(m):
    c, *a, r = input().split()
    C.append(int(c))
    A.append([int(i)-1 for i in a])
    R.append(r)

ans = 0
for mask in range(1 << n):
    ok = True
    for i in range(m):
        cnt = 0
        for a in A[i]:
            if (mask >> a) & 1 == 1:
                cnt += 1
        if R[i] == 'o' and cnt < k:
            ok = False
        if R[i] == 'x' and cnt >= k:
            ok = False
    if ok:
        ans += 1

print(ans)