#problem 1
def cal_exp_x(x, n):
    exp_x = 1.0
    fact = 1.0
    for i in range(1, n + 1):
        fact *= i
        exp_x += (x ** i) / fact
    return exp_x

#problem 2
def sum_S(n):
    S = 0
    fact = 1.0
    for i in range(1, n + 1):
        fact *= i
        S += 1 / fact
    return S

x = float(input("Nhap x: "))
n = int(input("Nhap n: "))
res1 = cal_exp_x(x, n)
print("Gia tri xap xi cua e^x la: ", res1)
res2 = sum_S(n)
print("Gia tri cua tong S la: ", res2)
