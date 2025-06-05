# dictionary - CRUD: Create - Read - Update - Delete

# Create - Khởi tạo
dict1 = {}
dict2 = {
    # Các cặp key - value
    'name' : 'Duc Trung',
    'age': 2,
    'gender': 'male'
}

# Read - Duyệt, hiện phần tử
    # Duyệt toàn bộ key-value
for key, value in dict2.items():
    print(f"{key}: {value}")
    # Truy cập bằng key
print('Tên:', dict2['name'])
    # Sử dụng phương thức get()
print('Tuổi:', dict2.get('age'))
        # Nếu không tồn tại key => None / Giá trị mặc định
print('Money:', dict2.get('money'))
print('Money:', dict2.get('money', '404 not found'))

# Update - chỉnh sửa
    # Thêm cặp key - value
dict2['children'] = 'Duc Trung mini'
    # Sửa cặp key - value
dict2['children'] = 'huy quần hoa'
print(dict2)

# Delete - xóa phần tử
    # del - xóa phần tử theo key
del dict2['children']
    # pop - xóa phần tử theo key, trả về giá trị
print(dict2.pop('gender'))
print(dict2)

# Kiểm tra key xem có tồn tại không
print('name' in dict2) # True
print('money' in dict2) # False

# Lấy tất cả cặp key - value: items()
print(dict2.items())
# Lấy tất cả key: keys()
print(dict2.keys())
# Lấy tất cả value: values()
print(dict2.values())