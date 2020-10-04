# BT3: Tổng 1^3+2^3...n^3
"""code"""
n = int(input("Nhập n:"))
def tinhtong(n):
    x = 0
    for i in range(1,n):
        i+=1
        x += pow(i,3)
    print(x)
tinhtong(n)