#!/usr/bin/env python3
n = int(input())

ans_pre = []
ans = []
for i in range(n):
    for j in range(i+1):
        if (i == j or j == 0) or ans_pre == []:
            ans.append(1)
        else:
            ans.append(ans_pre[j-1] + ans_pre[j])
    print(*ans)
    ans_pre = ans
    ans = []