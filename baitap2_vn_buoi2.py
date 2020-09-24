#BT3: Lập chương trình tính các tổng
x = float(input('Nhập số thực bất kì: '))
n = int(input('Nhập số nghuyên: '))

S = 0
S2 = 0
luythua = 1

for i in range(1,n+1):
    luythua = luythua * x
    S= S + luythua
print('kết quả',+S)


for i in range(1,n+1):
    if i == n+1:
        S2 = (-1)**i*(x**i)
    else:
        if i%2==0:
            S2+= x**i
        else:
            S2-= x**i
print("kết quả = ", 1+S2)