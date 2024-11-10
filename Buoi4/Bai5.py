import math
def binary_search(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        if a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

n = int(input("n = "))
a = []
for i in range(n):
    element = int(input())
    a.append(element)
a.sort()
x = int(input("x = "))
output = binary_search(a, x)
print("index = ", output)