def mix_list(a, b):
    c = []
    min_list = min(len(a), len(b))

    for i in range(min_list):
        c.append(a[i])
        c.append(b[i])

    if len(a) > min_list:
        c.extend(a[min_list:])

    if len(b) > min_list:
        c.extend(b[min_list:])

    return c

n = int(input("n = "))
a = []
for i in range(n):
    ai = input()
    a.append(ai)

m = int(input("m = "))
b = []
for i in range(m):
    bi = input()
    b.append(bi)

result = mix_list(a, b)
print(result)


# ------------------------------------------------------------------------
# Kiểm thử
# a dài hơn b
a = ['a', 'b', 'c', 'd']
b = [1, 2]
print(mix_list(a, b))  # Kết quả: ['a', 1, 'b', 2, 'c', 'd']

# a dài bằng b
a = ['a', 'b', 'c']
b = [1, 2, 3]
print(mix_list(a, b))  # Kết quả: ['a', 1, 'b', 2, 'c', 3]

# a ngắn hơn b
a = ['a', 'b']
b = [5, 6, 7, 8]
print(mix_list(a, b))  # Kết quả: ['a', 5, 'b', 6, 7, 8]

# a và b chứa toàn số
a = [10, 20, 30]
b = [1, 2, 3, 4]
print(mix_list(a, b))  # Kết quả: [10, 1, 20, 2, 30, 3, 4]

# a chứa chuỗi ký tự còn b chứa số
a = ['a', 'o', 'e']
b = [1, 2]
print(mix_list(a, b))  # Kết quả: ['a', 1, 'o', 2, 'e']