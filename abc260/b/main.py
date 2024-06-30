#!/usr/bin/env python3
n, x, y, z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = set()

for i in range(x):
    ans.add(A.index(max(A))+1)
    index = A.index(max(A))
    A[index] = -1
    B[index] = -1

for i in range(y):
    ans.add(B.index(max(B))+1)
    index = B.index(max(B))
    A[index] = -1
    B[index] = -1

sum_AB = [A[i]+B[i] for i in range(n)]
for i in range(z):
    ans.add(sum_AB.index(max(sum_AB))+1)
    sum_AB[sum_AB.index(max(sum_AB))] = -1

ans = list(ans)
ans.sort()
for i in range(len(ans)):
    print(ans[i])