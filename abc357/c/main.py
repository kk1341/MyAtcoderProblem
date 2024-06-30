#!/usr/bin/env python3

def larger_carpet(level):
    if level == 0:
        return '#'
    else:
        temp = []
        #carpetとして一つ下のレベルのカーペットを取得
        carpet = larger_carpet(level-1)
        #carpetを用いて与えられたレベルのカーペットを生成する
        for i in range(len(carpet)):
            temp.append(carpet[i]+carpet[i]+carpet[i])
        for i in range(len(carpet)):
            temp.append(carpet[i]+('.'*len(carpet))+carpet[i])
        for i in range(len(carpet)):
            temp.append(carpet[i]+carpet[i]+carpet[i])
        return temp


N = int(input())

print(*larger_carpet(N), sep='\n')