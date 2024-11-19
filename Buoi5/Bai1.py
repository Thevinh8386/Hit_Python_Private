A = tuple(int(i) for i in input("Nhập các số nguyên cho tuple A: ").split())
B = tuple(input("Nhập các xâu ký tự cho tuple B: ").split())

# a) Đếm số pt > tbc
sum = 0
for i in A:
    sum += i
tbc = sum/len(A)
dem = 0
for x in A:
    if x > tbc:
        dem+=1
print(f"Số phần tử trong A > tbc: {dem}")

# b) Chia tuple A thành hai tuple con: số chẵn và số lẻ
even_num = []
odd_num = []
for i in A:
    if i % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)

even_num = tuple(even_num)
odd_num = tuple(odd_num)
print(f"Tuple chứa các số chẵn: {even_num}")
print(f"Tuple chứa các số lẻ: {odd_num}")

# c) Nhập vào ký tự k và đếm số lần xuất hiện của k trong B
k = input("Nhập ký tự k: ")
dem_k = 0
for i in B:
    if i == k:
        dem_k += 1
print(f"Số lần xuất hiện của '{k}' trong tuple B: {dem_k}")

# d) Tìm các phần tử trong tuple B có độ dài >= 5 ký tự
length_string = []
for s in B:
    length_s = 0
    for _ in s:
        length_s += 1

    if length_s >= 5:
        length_string.append(s)
length_string = tuple(length_string)
print(f"Các phần tử trong B có độ dài >= 5 ký tự: {length_string}")

# e) Kết hợp tuple A + tuple B -> tuple mới C
C = []
if len(A) < len(B):
    length_C = len(A)
else:
    length_C = len(B)
for i in range(length_C):
    C.append((A[i], B[i]))
C = tuple(C)
print(f"Tuple C: {C}")