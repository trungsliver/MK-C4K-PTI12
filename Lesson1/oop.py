# Lập trình hướng đối tượng 
# OOP - Object oriented programming

# Tổng quát: OOP là cách ta mô phỏng thế giới thực vào chương trình máy tính

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Attribute (thuộc tính):       đặc điểm của đối tượng
# Method (phương thức):         hành động của đối tượng

# Khai báo class (lớp đối tượng tổng quát)
class Human:
    # Hàm khởi tạo attribute (thuộc tính)
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (attribute)
        self.name = name
        self.age = age
        self.gender = gender

    # Phương thức (hành động) - Method
    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}')

    # Phương thức hát
    def sing(self, song):
        print(f'Tôi đang hát bài {song}')

    # Phương thức tính năm sinh
    def dob(self):
        year = 2025 - self.age
        return year

human1 = Human('Duc Trung', 27, 'male')
human1.introduce()
human1.sing('Haru Haru')  
print(human1.dob())
