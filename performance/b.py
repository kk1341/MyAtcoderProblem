n, m = map(int, input().split())
d = [0] * n
route = []
for i in range(n):
    route.append([])

for i in range(m):
    a, b = map(int, input().split())
    route[a-1].append(b)
    route[b-1].append(a)
    d[a-1] += 1
    d[b-1] += 1

for i in range(n):
    print(d[i], *sorted(route[i]))