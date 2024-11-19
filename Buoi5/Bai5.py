docker_compose = {
    "version": "3.8",
    "services": {
        "app": {
            "image": "python:3.10-slim",
            "command": "python app.py",
            "volumes": "./app:/app",
            "restart": "always",
            "ports": "5000:5000",
            "depends_on": "db"
        }
    }
}

#1. In toàn bộ nội dung của dictionary
print("1. Toàn bộ nội dung dictionary: ")
print(docker_compose)

#2. Sửa version thành '3.10' và in kết quả
docker_compose["version"] = "3.10"
print("\n2. Sau khi sửa 'version':")
print(docker_compose)

#3. Lấy giá trị của key 'image' và in ra
image_value = docker_compose["services"]["app"]["image"]
print("\n3. Giá trị của key 'image':")
print(image_value)

#4. Thêm key 'environment' và in kết quả
docker_compose["services"]["app"]["environment"] = ["PYTHONUNBUFFERED=1"]
print("\n4. Sau khi thêm key 'environment':")
print(docker_compose)

#5. Kiểm tra xem dictionary có chứa key 'volumes' không
has_volumes = "volumes" in docker_compose["services"]["app"]
print("\n5. Dictionary có chứa key 'volumes'?")
print(has_volumes)

#6. Xóa key 'depends_on' và in kết quả
docker_compose["services"]["app"].pop("depends_on", None)
print("\n6. Sau khi xóa key 'depends_on':")
print(docker_compose)

#7. Đếm số lượng key trong dictionary
dem_key = len(docker_compose["services"]["app"])
print("\n7. Số lượng key trong dictionary:")
print(dem_key)

#8. Tạo list chứa tất cả các giá trị trong dictionary và in kết quả
values_list = list(docker_compose["services"]["app"].values())
print("\n8. List chứa tất cả các giá trị trong dictionary:")
print(values_list)

#9. Kiểm tra xem 'always' có phải là giá trị của bất kỳ key nào không
check_always = "always" in values_list
print("\n9. 'always' có phải là giá trị của bất kỳ key nào?")
print(check_always)

#10. Nhập một key và value từ bàn phím, thêm vào dictionary và in lại kết quả
new_key = input("\n10. Nhập 1 key mới: ")
new_value = input("Nhập giá trị tương ứng: ")
docker_compose["services"]["app"][new_key] = new_value
print("\nSau khi thêm key và value mới:")
print(docker_compose)
