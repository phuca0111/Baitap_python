
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
if  ((a<b+c) and (b<a+c) and (c<b+c) and (a>0) and (b>0) and (c>0)):
        if( (a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c== a*a+b*b)):
            print("Đây  Tam Giác Vuông")
        elif (a==b==c):
            print("Đây  Tam Giác Đều")
        elif (a==b or a==c or b==c):
            print("Đây  Tam Giác Cân")
        elif (a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b):
            print("Đây  Tam Giác Tù")
        else:
            print("Đây  Tam Giác Nhọn")
else:
    print(" đây Không phải tam Giác")