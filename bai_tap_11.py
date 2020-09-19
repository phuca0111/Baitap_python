#BT11: Viết chương trình tính chu vi và diện tích hình tròn sau khi người dùng nhập chiều dài bán kính (r)
"""code"""

r = int(input('Nhập bán kính:'))
pi = 3.14
CV = r*2*pi
DT = r*r*pi
print("Chu vi là:",CV)
print("Diện tích là:",DT)
