#Bài 3.4 Viết hàm với tham số truyền vào là một tháng và trả về mùa tương ứng trong năm. Sử dụng hàm vừa cài đặt, nhập vào một tháng và in ra màn hình mùa trong năm
n = int(input('Nhập tháng '))
def func_greet (n):
    if(1<=4 and n <4):
        print('mùa xuân')
    elif(4<=6 and n <= 6 and n >= 4):
        print('mùa hạ')
    elif (7<=9 and n <=9 and n >=7):
        print('mùa thu')
    elif(10<=12 and n <= 12):
        print('mùa đông')
func_greet(n)
