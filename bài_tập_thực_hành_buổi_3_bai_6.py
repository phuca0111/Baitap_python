#Bài 3.6 Viết hàm tính diện tích hình tròn với tham số truyền vào là bán kính; sử dụng hàm vừa cài đặt, nhập vào bán kính và in ra màn hình diện tích hình tròn.
import math

print("Hãy nhập bán kính hình tròn:")
r = float(input())
cv = 2*math.pi*r
dt = pow(r,2) 
print("Chu vi hình tròn bằng: ", cv)
print("Diện tích hình tròn bằng: ", dt)
