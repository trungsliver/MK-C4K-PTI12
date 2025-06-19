import oop

# Danh sách đối tượng
users_arr = [
    oop.User('ductrung', 'ductrung@gmail.com', '123456'),
    oop.User('duylong', 'duylong@gmail.com', '456789'),
    oop.User('phuongthuy', 'phuongthuy@gmail.com', '741852')
]

    # Chỉ print địa chỉ ô nhớ
# print(users_arr[0])
    # Dùng phương thức hiển thị thông tin
# users_arr[0].show_info()

# Test Database
userDB = oop.UserDatabase()

    # Độ dài 2 danh sách sau khởi tạo
print('users_list:', len(userDB.users_list))
print('users_dict:', len(userDB.users_dict))

    # Lấy dữ liệu cho users_list
userDB.convert_to_object()
print('users_list:', len(userDB.users_list))
print('users_dict:', len(userDB.users_dict))

    # Hiển thị toàn bộ dữ liệu
userDB.show_all()