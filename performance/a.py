n, m = map(int, input().split())
H = list(map(int, input().split()))

for i in range(len(H)):
    m -= H[i]
    if m < 0:
        print(i)
        exit()

print(len(H))