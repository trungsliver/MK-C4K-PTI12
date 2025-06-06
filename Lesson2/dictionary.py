# DICTIONARY & MAP
# Bài 1: Cho 1 danh sách gồm tên của học sinh (viết hoa lộn xộn)
# Yêu cầu: Dùng map() để chuyển đổi danh sách trên viết hoa tất cả chữ
# Ví dụ: tRunG -> TRUNG
pti12 = ['dUy LOng', 'pHuOnG ThUY', 'dUC tRuNg']
print(list(map(lambda name: name.upper(), pti12)))  

# Bài 2: Quản lý thông tin sinh viên
# #Yêu cầu: Tạo một dictionary lưu trữ thông tin sinh viên với các khóa: name, age, và grade. 
# Thực hiện các thao tác sau:
# 1. Thêm sinh viên với thông tin name = "John", age = 22, và grade = "A".
student = {
    "name": "John",
    "age": 22,
    "grade": "A"
}
# 2. Cập nhật grade của sinh viên thành "A+".
student["grade"] = "A+"
# 3. Xóa thông tin age của sinh viên.
del student["age"]
# 4. Kiểm tra xem name có trong dictionary không.
print("name" in student)

# Bài 3: Đếm Số Lần Xuất Hiện Của Từ Trong Chuỗi
# Yêu cầu: Viết chương trình nhận vào một chuỗi và trả về một dictionary đếm số lần xuất hiện của mỗi từ trong chuỗi.
sentence = 'this is a test this is only a test'
    # key là từ ở trong câu
    # value là số lần xuất hiện của từ đó
def count_words(sentence):
    # strip(): xóa khoảng trắng ở đầu và cuối
    # split(): chia chuỗi thành list các từ
    words = sentence.strip().split()
    count_dict = {}
    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1
    return count_dict
print(count_words(sentence))

# Bài 4: Gộp Hai Dictionary
# Yêu cầu: Cho hai dictionary A và B. Viết chương trình gộp chúng lại. Nếu một key xuất hiện ở cả hai dictionary, cộng giá trị của chúng lại.
A = {'a': 100, 'b': 200, 'c': 300}
B = {'b': 250, 'c': 150, 'd': 400}

def merge1(dict1, dict2):
    # copy dict1 để đảm bảo dữ liệu k bị thay đổi
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        # nếu key đã có trong dict1 thì cộng 2 giá trị lại
        # nếu key chưa tồn tại, để giá trị mặc định = value(dict2)
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict
print(merge1(A, B))

# Bài 5: Tìm Key Có Giá Trị Lớn Nhất
# Yêu cầu: Cho một dictionary có các cặp {key: value}. Viết chương trình để tìm key có giá trị lớn nhất.
    # Cách 1:
def find_max_key(dict1):
    # Khai báo value lớn nhất là value đầu tiên trong dict1
    max_value = list(dict1.values())[0]
    key_max = list(dict1.keys())[0]
    # Duyệt dict1
    for key, value in dict1.items():
        # Nếu value lớn hơn max_value thì cập nhật max_value và key_max
        if value > max_value:
            max_value = value
            key_max = key
    return key_max
print(find_max_key(A))
print(find_max_key(B))

    # Cách 2:
def find_max_key_2(dict1):
    # sử dụng max() với key để tìm key có giá trị lớn nhất
    return max(dict1, key = dict1.get)
print(find_max_key_2(A))
print(find_max_key_2(B))

# Bài 6: Sắp Xếp Dictionary Theo Giá Trị
# Yêu cầu: Viết chương trình để sắp xếp một dictionary theo giá trị từ cao đến thấp.
grade = {
    'Khải Hưng': 2,
    'Minh Tâm': 7,
    'Minh Đức': 6,
    'Khoa Nguyên': 5,
    'Hải meme': 10,
    'Bảo Nam': 4
}
def sort_dict_by_value(my_dict):
    # sử dụng sorted() với key để sắp xếp dictionary
    return dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print(sort_dict_by_value(grade))

# Bài 7: Nhóm Các Phần Tử Theo Giá Trị
# Yêu cầu: Viết chương trình để nhóm các phần tử của một dictionary dựa trên giá trị của chúng. Ví dụ, các phần tử có cùng giá trị sẽ được đưa vào một danh sách.
data = {
    'apple': 1,
    'banana': 2,
    'cherry': 2,
    'bomb': 3,
    'elderberry': 3
}

def group_by_value(dict1):
    # Khai báo một dictionary để lưu các phần tử có cùng giá trị
    group_dict = {}
    # Duyệt dictionary
    for key, value in dict1.items():
        # Nếu value chưa có trong group_dict thì tạo value là danh sách rỗng
        if value not in group_dict:
            group_dict[value] = []
        # Thêm key vào danh sách value
        group_dict[value].append(key)
    return group_dict
print(group_by_value(data))

# Bài 8: Tạo Dictionary Từ Danh Sách
# Yêu cầu: Viết chương trình tạo một dictionary từ hai danh sách: một danh sách chứa key và một danh sách chứa value tương ứng.
keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]
def list_to_dict(keys, values):
    # zip(): tạo ra các cặp key-value từ 2 danh sách
    # dict(): chuyển các cặp key-value thành dictionary
    return dict(zip(keys, values))
print(list_to_dict(keys, values))