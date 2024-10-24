a = int(input("a = "))
b = int(input("b = "))

print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a // b = ", a // b)
print("a ** b = ", a ** b)
print("a % b = ", a % b)

if a > b:   ("a lớn hơn b")
elif a < b: print("a nhỏ hơn b")
else:   print("a bằng b")

print("a AND b = ", a & b)
print("a OR b = ", a | b)
print("a XOR b = ", a ^ b)
print("NOT a == b là: ", ~(a == b))
print("a dịch phải 5 bit thành", a >> 5)
print("a dịch trái 6 bit thành", a << 6)
print("Hệ cơ số 2 đảo ngược của a là: ", bin(a)[:1:-1])


