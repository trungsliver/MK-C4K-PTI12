# Hàm map(function, itertable)
    # function: hàm biến đổi dữ liệu
    # itertable: bảng dữ liệu cần biến đổi

# Ví dụ: Cho danh sách học sinh
# Yêu cầu: dùng map() để thêm 'MindX' vào sau tên hsinh
arr = ['Long', 'Thúy', 'Trung', 'Vân', 'Hà']
    # Cách 1: Dùng hàm xác định
def convert_name(student):
    return student + ' MindX'
arr1 = map(convert_name, arr)
print(list(arr1))

    # Cách 2: Dùng lambda - hàm không xác định / ẩn danh
arr2 = map(lambda name: name + ' MindX', arr)
print(list(arr2))

        # Giải thích
arr3 = []
for name in arr:
    new_name = name + ' MindX'
    arr3.append(new_name)
print(arr3)

# Bài tập: Cho 1 danh sách điểm hệ số 10 (thang điểm 10)
# Yêu cầu: dùng map() để chuyển đổi toàn bộ phần tử danh sách sang điểm hệ số 4 (thang 4)
gpa10 = [5, 7, 8, 10, 9]
    # Cách 1: Dùng hàm xác định
def convert_gpa(score):
    return round((score / 10) * 4, 2)
gpa_4 = list(map(convert_gpa, gpa10))
print(gpa_4)

    # Cách 2: Dùng hàm không xác định
gpa_4_2 = map(lambda gpa: round((gpa / 10) * 4, 2), gpa10)
print(list(gpa_4_2))