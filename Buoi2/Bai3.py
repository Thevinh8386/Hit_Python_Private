print("Chao mung den CLB Tin Hoc HIT")
print("CLB Tin Hoc HIT truc thuoc Khoa CNTT - \"10 diem\"")

str = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
upper_char = ''
for i in str:
    if i.isupper():
        upper_char += i
print("Các chữ cái in hoa trong chuỗi là: ", upper_char)

lower_char = ''
for i in str:
    if i.islower():
        lower_char += i
print("Các chữ cái in thường trong chuỗi là: ", lower_char)

check_CNTT = "CNTT" in str
if check_CNTT:   print("YES")
else:            print("NO")

upper_to_lower = str.swapcase()
print("Chuỗi sau khi đổi chữ hoa -> thường và ngược lại:", upper_to_lower)
