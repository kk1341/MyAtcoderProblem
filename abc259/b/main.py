#!/usr/bin/env python3
import math
a, b, d = map(int, input().split())
d = math.radians(d)
print(f'{a*math.cos(d) - b*math.sin(d)} {a*math.sin(d) + b*math.cos(d)}')