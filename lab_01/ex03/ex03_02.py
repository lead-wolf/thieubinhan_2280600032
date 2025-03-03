def daonguoclist(lst):
    return lst[::-1]

#nhập danh sách từ người dùng avf xử lý chuỗi
input_List = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_List.split(',')))

#sử dụng hàm và in kết quả
list_dao_nguoc = daonguoclist(numbers)
print("List sau khi đảo ngược là:", list_dao_nguoc)
