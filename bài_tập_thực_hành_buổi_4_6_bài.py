# Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
# Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
# Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
# Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, 
# nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
# Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
# Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
"""code bài 1"""

# KT=input("Nhap chuoi: ")
# def thaythe(KT):
#     x=KT[0]
#     for i in range(1,len(KT)):
#         if (KT[i] == KT[0]):
#             x+="$"
#         else:
#             x+=KT[i]
#     return x
# print('chuỗi sau khi được thay thế',thaythe(KT))
"""code bài 2"""
# kytu =input("Nhap chuoi:")
# i=0
# def xoakytu(kytu):
#     n=kytu[:i]+kytu[i+1:]
#     print(n)
# i=int(input("Nhap vi tri xoa:"))
# xoakytu(kytu)
""" code bài 3"""
# kytu=input("Nhap chuoi:")
# def xoakitule(kytu):
#     return kytu[::2]
# print(xoakitule(kytu)) 
""" code bài 4"""
# kytu= input("Nhap chuoi:")
# def noikytudaucuoi(kytu):
#     if len(kytu)<2:
#         return " "
#     else:
#         return Line[0:2]+Line[-2:]
# Line= input("Nhap chuoi:")
# print(noikytudaucuoi(kytu))
""" code bài 5 """
# kytu=input("Nhap chuoi:")
# def kytunhonhatlonnhat(line):
#     max=min=kytu[0]
#     for i in kytu:
#         if min>i:
#             min=i
#         if max<i:
#             max=i
#     print("Ki tu lon nhat trong chuoi la",max)
#     print("ki tu nho nhat trong chuoi la",min)
# kytunhonhatlonnhat(kytu)
"""code bài 6"""
# kytu=input("Nhap chuoi: ")
# def daonguockytuhoathuong(kytu):
#     x = ""
#     for i in kytu:
#         if i.islower():
#             x+=i.upper()
#         else:
#             x+=i.lower()
#     print(x)
# daonguockytuhoathuong(kytu)

