import re
email = input("Nhập vào 1 email: ")
pattern = r'^\w+@\w+\.\w+$'
if re.match(pattern, email):
    print("Valid")
else:
    print("Invalid")
