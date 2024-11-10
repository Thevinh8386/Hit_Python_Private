def common_nums(nums1, nums2):
    dem1 = {}
    for i in nums1:
        if i in dem1:
            dem1[i] += 1
        else:
            dem1[i] = 1

    dem2 = {}
    for i in nums2:
        if i in dem2:
            dem2[i] += 1
        else:
            dem2[i] = 1

    result = []
    for i in dem1:
        if i in dem2:
            min_dem = min(dem1[i], dem2[i])
            result.extend([i] * min_dem)
    return result

n = int(input("Nhap so phan tu nums1: "))
nums1 = []
for i in range(n):
    num1 = int(input())
    nums1.append(num1)

m = int(input("Nhap so phan tu nums2: "))
nums2 = []
for i in range(m):
    num2 = int(input())
    nums2.append(num2)

output = common_nums(nums1, nums2)
reversed_output = list(reversed(output))
if reversed_output != output:
    print(output, reversed_output)
else:
    print(output)



