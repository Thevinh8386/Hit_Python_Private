dang_ky = set(input("Nhập danh sách các bạn đã đăng ký: ").split())
check_in = set(input("Nhập danh sách các bạn đã check-in: ").split())

# a) In ra danh sách các bạn chưa check-in
chua_check_in = dang_ky - check_in
print(f"Danh sách các bạn chưa check-in: {chua_check_in}")

# b) Tính toán tổng số lượng các bạn đã đăng ký và đã check-in
total = len(dang_ky & check_in)
print(f"Tổng số lượng các bạn đã đăng ký và đã check-in: {total}")

# c) Sắp xếp danh sách các bạn đã đăng ký theo thứ tự từ điển
sort_list = sorted(dang_ky)
print(f"Danh sách các bạn đã đăng ký theo thứ tự từ điển: {sort_list}")