import math
def is_chinh_phuong(x):
    if x < 0:
        return False
    can = int(math.sqrt(x))
    if can * can == x:
        return True

n = int(input("Nhap so nguyen duong n: "))
count = 0
for i in range(2, n):
    if is_chinh_phuong(i):
        count += 1
print(count)