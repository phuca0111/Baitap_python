# BT7: Viết hàm kiểm tra só chính phương
"""code"""
def Sochinhphuong():
  n =  int(input("Nhập n: "))
  i =0
  while i * i <= n:
    if i * i == n:
      print("Số này là số chính phương")
      return 0
    i+=1
  print("Số này không phải là số chính phương")  
Sochinhphuong()
