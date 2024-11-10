import math
def MAE(n, a):
    loss  = 0
    for i in len(a):
        loss += abs(a[i][0] - a[i][1])
    loss /= n
    return loss

def MSE(n, a):
    loss  = 0
    for i in len(a):
        loss += (a[i][0] - a[i][1])**2
    loss /= n
    return loss

def RMSE(n, a):
    return math.sqrt(MSE(n, a))

def Huber_Loss(n, a, s):
    loss = 0
    for i in len(a):
        h = abs(a[i][0] - a[i][1])
        if h <= s:
            loss += 0.5 * h**2
        else:
            loss += s * ( h - 0.5 * s)
    loss /= n
    return loss

n = int(input("n = "))
a = [[float(input()) for _ in range(2)] for _ in range(n) ]
print(f"{a}")

loss_name = input("Nhap loss name (MAE, MSE, RMSE, Huber_Loss): ")
if loss_name == "MAE":
    result = MAE(n, a)
elif loss_name == "MSE":
    result = MSE(n, a)
elif loss_name == "RMSE":
    result = RMSE(n, a)
elif loss_name == "Huber_Loss":
    s = float(input("Nhap delta for Huber Loss: "))
    result = Huber_Loss(n, a, s)
else:
    print(f"{loss_name} loss is not supported")
    result = None

if result is not None:
    print(f"{loss_name}: {result}")