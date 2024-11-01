import math

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def binary_step(x):
    return 1 if x >= 0 else 0

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def elu(x):
    alpha = float(input())
    if x < 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x

x = input()
if not is_number(x):
    print("x must be a number")

x = float(x)
print("Input activation function ( binary | sigmoid | elu ) : ")
activation_function = input()

if activation_function == 'binary':
    result = binary_step(x)
    print(f"binary: f({x}) = {result}")
elif activation_function == 'sigmoid':
    result = sigmoid(x)
    print(f"sigmoid: f({x}) = {result}")
elif activation_function == 'elu':
    result = elu(x)
    print(f"elu: f({x}) = {result}")
else:
    print(f"{activation_function} is not supported")
