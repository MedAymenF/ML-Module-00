#!/usr/bin/env python3
from TinyStatistician import TinyStatistician
a = [1, 42, 300, 10, 59]
stat = TinyStatistician()
print(stat.mean(a))
# Output:
# 82.4
print(stat.median(a))
# Output:
# 42.0
print(stat.quartile(a))
# Output:
# [10.0, 59.0]
print(stat.percentile(a, 10))
# Output:
# 1.0
print(stat.percentile(a, 28))
# Output:
# 10.0
print(stat.percentile(a, 83))
# Output:
# 300.0
print(stat.var(a))
# Output:
# 12279.4399...
print(stat.std(a))
# Output:
# 110.8126
