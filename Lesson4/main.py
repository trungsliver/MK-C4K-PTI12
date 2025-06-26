import oop

# Khởi tạo dữ liệu (database)
dtb = oop.PlayerDatabase()

# Load data vào danh sách object
dtb.convert_to_object()

# Kiểm tra dữ liệu
print("players_dict:", len(dtb.players_dict))
print("players_list:", len(dtb.players_list))
dtb.show_all()

# Tìm kiếm theo tên
def find_by_name(name):
    find1 = dtb.find_player_by_name(name)
    # Tìm thấy
    if find1 != False:
        find1.show_info()
    else:
        print("Không tìm thấy player có tên:", name)

find_by_name("Cristiano Ronaldo")
find_by_name("Duc Trung")

# Thêm 1 data mới
new_player = {
        "id": 99999999,
        "name": "Duc Trung",
        "dob": "07/08/1998",
        "region": "Vietnam",
        "club": "MindX",
        "rating": 5,
        "worth": 9999999.0
}
# dtb.add_player(new_player)

# Sửa theo tên
edit_player1 = {
        "id": 99999999,
        "name": "Duc Trung hihi",
        "dob": "07/08/1998",
        "region": "Vietnam",
        "club": "MindX",
        "rating": 5,
        "worth": 9999999.0
}
dtb.edit_player("Cristiano Ronaldo", edit_player1)
