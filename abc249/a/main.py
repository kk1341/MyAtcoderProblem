#!/usr/bin/env python3
a, b, c, d, e, f, x = map(int, input().split())
run_sec1 = 0
run_sec2 = 0
x1 = x
while True:
    if x1 <= a:
        if x1 <= 0:
            pass
        else:
            run_sec1 += x1
        break
    else:
        run_sec1 += a
        x1 -= (a+c)


x2 = x
while True:
    if x2 <= d:
        if x2 <= 0:
            pass
        else:
            run_sec2 += x2
        break
    else:
        run_sec2 += d
        x2 -= (d+f)

if run_sec1*b > run_sec2*e:
    print('Takahashi')
elif run_sec1*b < run_sec2*e:
    print('Aoki')
else:
    print('Draw')

#===================#
#模範解答1
# a, b, c, d, e, f, x = map(int, input().split())
# takahashi, aoki = 0, 0
# for k in range(x):
#     if k % (a + c) < a:
#         takahashi += b
#     if k % (d + f) < d:
#         aoki += e

# if takahashi > aoki:
#     print('Takahashi')
# elif takahashi < aoki:
#     print('Aoki')
# else:
#     print('Draw')

#模範解答2
# def solve(a, b, c, x):
#     q = x // (a + c)
#     r = x % (a + c)
#     return (q*a + min(a, r)) * b

# a, b, c, d, e, f, x = map(int, input().split())
# takahashi = solve(a, b, c, x)
# aoki = solve(d, e, f, x)

# if takahashi > aoki:
#     print('Takahashi')
# elif takahashi < aoki:
#     print('Aoki')
# else:
#     print('Draw')

#===================#