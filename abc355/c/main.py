#!/usr/bin/env python3
n, t = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
row = [0] * n
col = [0] * n
diag = [0] * 2

for i in range(t):

    x = A[i] // n
    y = A[i] % n

    #横
    row[x] += 1
    if row[x] == n:
        print(i+1)
        exit()

    #縦
    col[y] += 1
    if col[y] == n:
        print(i+1)
        exit()

    #右斜めおり
    if x == y:
        diag[0] += 1
        if diag[0] == n:
            print(i+1)
            exit()
    
    #左斜めおり
    if x + y == n - 1:
        diag[1] += 1
        if diag[1] == n:
            print(i+1)
            exit()

print(-1)
