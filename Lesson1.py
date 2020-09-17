#BT1.1: thông tin SV
""" code """
"""
Name = " Trần Phan Tấn Phúc"
Mssv = 1906020146
lop = "13THC"
teacher = "Nguyen Minh tan "
print("Xin chao thay :",teacher,"\n Em ten :",Name,"\n MSSV :",Mssv,"\n Học lop",lop,)
"""
  
#BT1.2: viếc chương trình nhập vào hai số nguyên , in ra màn hình tổng bình phương của 2 số nguyên
"""code"""
"""
a=12
b=45
S = a*a+b*b
print("Kết quả là :",S)
"""
#BT1.3: viết chương trình nhập vào tiền lương cơ bản , phụ cấp và số ngày đi làm trong tháng,in ra màn hình lương chính nhận được theo công thức:nhập tiền lương cơ bản , phụ cấp và số ngày đi làm lương chính = ((lương cơ bản + phụ cấp)/22)*số này đi làm
"""code"""
"""
Luongcb = int(input('Nhập mức lương của bạn:'))
Phucap = int(input('Phụ cáp của bạn:'))
Songaydilam = int(input('Nhập số ngày đi làm:'))
S=((Luongcb + Phucap)/22) * Songaydilam
print("Lương của bạn là",S)
"""
#BT1.4: Viết chương trình tính chu vi và diện tích hình tròn sau khi người dùng nhập chiều dài bán kính (r)
"""code"""
"""
r = int(input('Nhập bán kính:'))
pi = 3.14
CV = r*2*pi
DT = r*r*pi
print("Chu vi là:",CV)
print("Diện tích là:",DT)
"""
# bài tập về nhà
#BT1: viết chương trình in ra màn hình chữ "xin chào"
"""code"""
"""
print("hello")
"""
# BT1.5: viết chương trình nhập một số gồm hai chữ số in ra màn hình số hàng đơn vị và số hàng chục 
"""code"""
"""
a = int(input('Nhập vào'))
dv = a%10
Hangchuc = a//10
print("Số hàng đơn vị là ",dv,"\n số hàng chục là",Hangchuc)
"""
#BT1.6: Viếc chương trình nhập họ tên sinh viên,MSSV , tuổi . sau đó cho biết họ tên SV , Mssv , tuôi là kiểu dữ liệu gì
"""code"""
"""
Name = input('Nhập tên của bạn: ')
Mssv = input('Nhập MSSV: ')
Tuổi = int(input('Nhập tuổi: '))
print(type(Name))
print(type(Mssv))
print(type(Tuổi))
"""
#BT1.7: viếc chương trình nhập họ tên sinh viên đếm chiều dài chuỗi và in ra ký tụ ở vị trí thứ 1
"""code"""
"""
Name = input('Nhập họ tên bạn: ')
dem = Name
print('Do dai cua', dem, 'la', len(dem))
kitu = Name
print("kí tự 1 là :",kitu[1])
"""

#BT1.8: nhập vào số 2 chữ số in ra số ngược lại 
"""code"""
"""
a = int(input('Nhập vào'))
a = int(str(a)[::-1])
print(a)
"""
#BT2.1: in câu hello python ra màn hình
"""code"""
"""
print("hello python")
"""
#BT2.2: in tên của ban ra màn hình
"""code"""
"""
print(" Trần Phan Tấn Phúc")
"""
#BT2.3: in thông tin cá nhân
"""code"""
"""
Name = " Trần Phan Tấn Phúc"
Mssv = 1906020146
lop = "13THC"
teacher = "Nguyen Minh tan "
print("Xin chao thay :",teacher,"\n Em ten :",Name,"\n MSSV :",Mssv,"\n Học lop",lop,)
"""
#BT2.4: Cộng trừ 2 số nguyên
"""code"""
"""
n1 = 12
n2 = 33
S= n1+n2
print("kết quả",S)
"""
#BT2.5: xuất kết quả hình chữ nhật bằng dấu *
"""code"""
"""
print("***********")
print("***********")
print("***********")
print("***********")
"""
#BT2.6: xuất kết quả hình chữ nhật bằng dấu * bên trong rỗng
"""code"""
"""
print("***********")
print("*         *")
print("*         *")
print("***********")
"""
#BT2.7: xuất kết quả hình tam giác bằng dấu *
"""code"""
"""
print("      *      ")
print("     ***     ")
print("    *****    ")
print("   *******   ")
print("  *********  ")
print(" *********** ")
print("*************")
"""