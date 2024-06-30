#!/usr/bin/env python3
n = int(input())
s, t = [], []
for i in range(n):
    u, v = input().split()
    s.append(u)
    t.append(v)

for i in range(n):
    can_give_a_nickname = False
    for S in [s[i], t[i]]:
        s_ok = True
        for j in range(n):
            if i != j:
                if S == s[j] or S == t[j]:
                    s_ok = False
        if s_ok:
            can_give_a_nickname = True
    if can_give_a_nickname == False:
        print('No')
        exit()

print('Yes')