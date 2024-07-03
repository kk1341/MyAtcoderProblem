#!/usr/bin/env python3
s = input()
player = [
    ['tourist', 3858],
    ['ksun48', 3679],
    ['Benq', 3658],
    ['Um_nik', 3648],
    ['apiad', 3638],
    ['Stonefeang', 3630],
    ['ecnerwala', 3613],
    ['mnbvmar', 3555],
    ['newbiedmy', 3516], 
    ['semiexp', 3481]
]

for i in range(10):
    if s == player[i][0]:
        print(player[i][1])
        exit()