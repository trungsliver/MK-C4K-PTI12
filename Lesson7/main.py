import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# xử lý
app = QApplication(sys.argv)
# Khai báo danh sách dữ liệu
arr = ['Nguyễn Phương Thúy', 'Nguyễn Duy Long', 'Bùi Đức Trung']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lesson7.ui',self)
        # Thêm danh sách để hiển thị lên listWidget
        self.listWidget.addItems(arr)
        # Khai báo sự kiện ấn nút
        self.btn_add.clicked.connect(self.add_item)
        self.btn_edit.clicked.connect(self.edit_item)
        self.btn_delete.clicked.connect(self.delete_item)
        self.btn_search.clicked.connect(self.search_item)

    def add_item(self):
        # Lấy dữ liệu từ lineEdit
        text = self.lineEdit_username.text().strip()
        # Thêm dữ liệu vào danh sách
        if text == '':
            msg_box('Lỗi', 'Nhập thiếu thông tin')
        else:
            # Thêm phần tử vào danh sách
            arr.append(text)
            # Xóa hết các phần tử cũ trên listWidget
            self.listWidget.clear()
            # Thêm danh sách để hiển thị lên listWidget
            self.listWidget.addItems(arr)
            # Xóa dữ liệu trong lineEdit
            self.lineEdit_username.setText('')
            
    def edit_item(self):
        # Lấy index dòng đang chọn trên listWidget
        cur = self.listWidget.currentRow()
        # Lấy text ở lineEdit
        text = self.lineEdit_username.text().strip()
        # Thay thế phần tử tại vị trí index
        if cur != -1 and text != '':
            arr[cur] = text
            msg_box('Thành công', 'Đã sửa thành công')
        else:
            msg_box('Lỗi', 'Chưa chọn dữ liệu cần sửa hoặc thiếu nội dung')
        # Xóa hết các phần tử cũ trên listWidget
        self.listWidget.clear()
        # Thêm danh sách để hiển thị lên listWidget
        self.listWidget.addItems(arr)
        # Xóa dữ liệu trong lineEdit
        self.lineEdit_username.setText('')

    def delete_item(self):
        # Lấy index dòng đang chọn trên listWidget
        cur = self.listWidget.currentRow()
        # Thay thế phần tử tại vị trí index
        if 0 <= cur <= len(arr):
            arr.pop(cur)
            msg_box('Thành công', 'Đã xóa thành công')
        else:
            msg_box('Lỗi', 'Chưa chọn dữ liệu cần xóa')
        # Xóa hết các phần tử cũ trên listWidget
        self.listWidget.clear()
        # Thêm danh sách để hiển thị lên listWidget
        self.listWidget.addItems(arr)
        # Xóa dữ liệu trong lineEdit
        self.lineEdit_username.setText('')

    def search_item(self):
        text = self.lineEdit_username.text().strip()
        check = False
        check_list = []
        for item in arr:
            if text in item:
                check = True
                check_list.append(item)
        # Xóa hết phần tử trên list widget
        self.listWidget.clear()
        # Thêm danh sách để hiển thị lên listWidget
        if check == True:
            msg_box('Thành công', f'Có {len(check_list)} kết quả')
        else:
            check_list.append('item not found')
        self.listWidget.addItems(check_list)

# Hàm hiển thị thông báo
def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Chuyển cửa sổ giao diện
def switch_window(classw):
    global window
    window = classw
    window.show()

# Run app
window = MainWindow()
window.show()
sys.exit(app.exec())