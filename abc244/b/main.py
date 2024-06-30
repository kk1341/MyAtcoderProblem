#!/usr/bin/env python3
n = int(input())
t = input()
ans = [0, 0]
R_cnt = 0

def run(r, ans):
    if r == 0:
        ans[0] += 1
    elif r == 1:
        ans[1] -= 1
    elif r == 2:
        ans[0] -= 1
    else:
        ans[1] += 1
    
    return ans

for i in range(n):
    if t[i] == 'R':
        if R_cnt == 3:
            R_cnt = 0
        else:
            R_cnt += 1
    else:
        ans = run(R_cnt, ans)

print(f'{ans[0]} {ans[1]}')