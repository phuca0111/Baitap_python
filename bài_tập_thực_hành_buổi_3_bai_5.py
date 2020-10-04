#Bài 3.5 Viết hàm tìm số lớn nhất của hai số nguyên a và b; sử dụng hàm vừa cài đặt, nhập vào 3 số nguyên a, b, c và tìm số lớn nhất trong 3 số đó.
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('nhập c: '))
def func_greet (a,b,c):
    print('So lon nhat la:', max(a,b,c))
func_greet(a,b,c)