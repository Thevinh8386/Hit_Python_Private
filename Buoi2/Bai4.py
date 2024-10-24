name = input("Nhập họ và tên: ")
age = int(input("Nhập tuổi: "))
gender = input("Nhập giới tính: ")
marital_status = input("Nhập tình trạng hôn nhân: ")

print("\nThông tin nhân khẩu học của bạn HIT 15: ")
print("Họ và tên: ", name)
print("Tuổi: ", age)
print("Giới tính: ", gender)
print("Tình trạng hôn nhân: ", marital_status)

if marital_status.lower() == "độc thân" and gender.lower() == "nữ":
    print("\nCó thể ghép đôi!")
else:
    print("\nKhông phù hợp!")
