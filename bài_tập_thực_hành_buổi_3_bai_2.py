#Bài 3.2 Viết hàm với tham số truyền vào là năm sinh, sử dụng hàm vừa cài đặt, nhập vào năm sinh và in ra tuổi:
ten = str(input('Nhập tên của bạn: '))
NS = int(input('Nhập năm sinh của bạn: '))
tuoi = 2020 - NS
def func_greet(ten,NS,Tuoi):
    print(f"Hello bạn: {ten}.bạn sinh năm: {NS}.tuoi bạn là: {tuoi} ")
    
func_greet(ten,NS,tuoi)

