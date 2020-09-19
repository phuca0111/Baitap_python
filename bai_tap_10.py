#BT10: viết chương trình nhập vào tiền lương cơ bản , phụ cấp và số ngày đi làm trong tháng,in ra màn hình lương chính nhận được theo công thức:nhập tiền lương cơ bản , phụ cấp và số ngày đi làm lương chính = ((lương cơ bản + phụ cấp)/22)*số này đi làm
"""code"""

Luongcb = int(input('Nhập mức lương của bạn:'))
Phucap = int(input('Phụ cáp của bạn:'))
Songaydilam = int(input('Nhập số ngày đi làm:'))
S=((Luongcb + Phucap)/22) * Songaydilam
print("Lương của bạn là",S)
