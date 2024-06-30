#!/usr/bin/env python3
s_ans = {'H': 0 , '2B': 0 , '3B': 0 , 'HR': 0}
for i in range(4):
    s_ans[input()] += 1

flag = True
for c in s_ans.values():
    if c != 1:
        flag = False
        break

print('Yes' if flag else 'No')

