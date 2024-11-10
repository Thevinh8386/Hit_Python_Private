def build_matrix(a, n, m):
    if len(a) < n * m:
        return "Không thể xây dựng được ma trận."

    matrix = [a[i * m:(i + 1) * m] for i in range(n)]
    return matrix

k = int(input("k = "))
a = []
for i in range(k):
    element = int(input())
    a.append(element)

n = int(input("n = "))
m = int(input("m = "))

result = build_matrix(a, n, m)
print(result)