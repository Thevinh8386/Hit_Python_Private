import random
def create_account(N):
    major = ['CNTT', 'KHMT', 'KTPM', 'HTTT', 'DAPT']
    list_account = {}

    for i in range(N):
        # Random maSV
        ma_SV = f"202360{str(i + 1).zfill(4)}"
        major_random = random.choice(major)

        # Password
        mat_khau = major_random + ma_SV

        # Lưu vào dictionary
        list_account[f"Account{i + 1}"] = {
            "Username": ma_SV,
            "Password": mat_khau
        }
    return list_account

N = int(input("Nhập số lượng tài khoản cần tạo: "))
if 1 <= N <= 100:
    account_club = create_account(N)
    for account, details in account_club.items():
        print(f"{account}: {details}")
else:
    print("Số lượng tài khoản phải trong [1, 100].")
