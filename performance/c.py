import bisect
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
ans = 0
pos = 0
for i in range(n):
    if pos == m:
        break
    if A[i] >= B[pos]:
        ans += A[i]
        pos += 1

print(ans if pos == m else -1)