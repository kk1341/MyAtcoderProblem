#!/usr/bin/env python3
prime = [True]*201
prime[0] = False
prime[1] = False
for p in range(15):
    if prime[p]:
        for i in range(p*p, 201, p):
            prime[i] = False

a, b, c, d = map(int, input().split())
for x in range(a, b+1):
    #高橋君が選んだ一つの数字に対して青木さんが選びうるすべての数字を探索
    #そのすべての対応がFalseであれば合成数しか作れない数字が存在するので，高橋君の勝利
    if all(not prime[x+y] for y in range(c, d+1)):
        print('Takahashi')
        exit()

print('Aoki')