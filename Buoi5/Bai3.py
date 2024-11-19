enter_dict = eval(input("Nhập dictionary: "))
new_dict = {}
for key, val in enter_dict.items():
    if val in new_dict:
        print("None")
    new_dict[val] = key
print(new_dict)