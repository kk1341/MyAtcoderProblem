#!/usr/bin/env python3
import math
a, b = map(int, input().split())
length = math.sqrt(a**2 + b**2)
print(f'{a/length} {b/length}')