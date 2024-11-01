n = int(input("Nhap so ban: "))
members = []
for i in range(n):
    name = input("Nhap ten thanh vien: ")
    mark1 = int(input("Diem bai 1: "))
    mark2 = int(input("Diem bai 2: "))
    total = mark1 + mark2
    if total >= 190:
        rating = "Xuất sắc"
    elif total >= 150:
        rating = "Giỏi"
    elif total >= 100:
        rating = "Khá"
    else:
        rating = "Yếu"
    members.append(f"{i + 1} {name} {total} {rating}")

for i in members:
    print(i)