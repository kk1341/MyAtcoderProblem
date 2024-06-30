#!/usr/bin/env python3

def base_n(num_10,n):
    str_n = ''
    if num_10 == 0:
        return 0
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

n = int(input())-1
n_5 = base_n(n, 5)
print(n_5*2)