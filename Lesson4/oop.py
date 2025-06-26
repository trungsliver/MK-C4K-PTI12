import data_io
import operator

class Player:
    def __init__(self, id, name, dob, region, club, rating = None, worth = None):
        self.id = id
        self.name = name
        self.dob = dob
        self.region = region
        self.club = club
        # Nếu có dữ liệu thì định dạng float, không có thì mặc định = 0
        self.rating = float(rating) if rating else 0.0
        self.worth = float(worth) if worth else 0.0

    def update(self, new_data:dict):
        for key, value in new_data.items():
            # Chỉ khi nào có thuộc tính thì mới update
            if value:
                setattr(self, key, value)

    def show_info(self):
        print(f"""====================
ID: {self.id}
Name: {self.name}
DOB: {self.dob}
Region: {self.region}
Club: {self.club}
Rating: {self.rating}
Worth: {self.worth}
====================""")      

# p1 = Player(1, 'Trung', '07/08/1998', 'Vietnam', 'MindX', 5, 9999)
# p2 = Player(2, 'Long', '07/08/1998', 'Vietnam', 'MindX')
# p3 = Player(id = 3, 
#             name = 'Thúy',
#             dob = '07/08/1998', 
#             region = 'Vietnam',
#             club = 'MindX')

# p1.show_info()
# p2.show_info()
# p3.show_info()


class PlayerDatabase:
    def __init__(self):
        # Danh sách dạng object
        self.players_list = list()
        # Danh sách dạng json / dictionary
        # self.players_dict = data_io.load_json_data()
        self.players_dict = data_io.load_json_data2('data.json')

    # Chuyển đổi từ json / dictionary => object
    def convert_to_object(self):
        new_players = []
        for player_data in self.players_dict:
            player = Player(id      = player_data["id"],
                            name    = player_data['name'],
                            dob     = player_data['dob'],
                            region  = player_data['region'],
                            club    = player_data['club'],
                            rating  = player_data['rating'],
                            worth   = player_data['worth'])
            new_players.append(player)
        self.players_list = new_players

    # Chuyển từ object => dictionary / json
    def convert_to_dict(self):
        json_data = list()
        for player in self.players_list:
            json_data.append(player.__dict__)
        return json_data

    # Hiển thị tất cả
    def show_all(self):
        for player in self.players_list:
            player.show_info()

    # Tìm kiếm bằng thuộc tính name
    def find_player_by_name (self, name):
        for player in self.players_list:
            # Tìm thấy
            if player.name == name:
                # Trả về dạng object
                return player
            # Không tìm thấy
            else:
                return False
            
    # Thêm 1 player mới
    def add_player(self, player_dict):
        # Chuyển player_dict sang dạng object
            # id sẽ là số index tiếp theo
        player_dict["id"] = len(self.players_list) + 1
        new_player = Player(id      = player_dict["id"],
                            name    = player_dict['name'],
                            dob     = player_dict['dob'],
                            region  = player_dict['region'],
                            club    = player_dict['club'],
                            rating  = player_dict['rating'],
                            worth   = player_dict['worth'])
        # Thêm vào danh sách object
        self.players_list.append(new_player)
        # Thêm vào danh sách dictionary
        self.players_dict.append(new_player.__dict__)
        # Ghi lại vào file json 
        # data_io.write_json_data(self.players_dict)
        data_io.write_json_data2(self.players_dict, 'data.json')

    # Tìm player theo tên và sửa thông tin
    def edit_player(self, edit_name, new_dict):
        # Tìm player
        matched = self.find_player_by_name(edit_name)
        # Sửa đối tượng
        if matched:
            # Sửa thông tin
            matched.update(new_dict)
            # sửa lại danh sách dictionary và file json
            self.players_dict = self.convert_to_dict()
            data_io.write_json_data2(self.players_dict, 'data.json')


    # Tìm player theo tên và xóa thông tin
    def delete_player(self, delete_name):
        # Tìm đối tượng
        matched = self.find_player_by_name(delete_name)
        # Xóa đối tượng
        if matched:
            self.players_list.remove(matched)
            # viết lại file json khi chỉnh sửa đối tượng
            self.players_dict = self.convert_to_dict()
            data_io.write_json_data(self.players_dict)

    # Tìm tên tất cả player có tên là search_name
    def search_player(self, search_name) -> list[Player]:
        matched_items = []
        for player in self.players_list:
            if search_name.lower() in player.name.lower():
                matched_items.append(player)
        return matched_items
    
    # Phương thức sắp xếp theo rating
    def sort_item_by_rating(self, top=None):
        self.players_list = sorted(self.players_list, 
                                      key=operator.attrgetter('rating'),
                                      reverse=True
                                      )
        if top:
            return self.players_list[top]
        
    # Phương thức sắp xếp theo name    
    def sort_item_by_title(self, top=None):
        self.players_list = sorted(self.players_list, 
                                      key=operator.attrgetter('name')
                                      )
        if top:
            return self.players_list[top]