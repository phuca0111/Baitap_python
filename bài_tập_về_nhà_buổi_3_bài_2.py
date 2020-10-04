# BT2: Tính n!
"""code"""
n = int(input("Nhập số cần tính giai thừa: "))
def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
giaiThua(n)