# BT5: Tính tổng các số chẵn
"""code"""
def Tongchan():
  n= int(input("Nhập số chẵn: "))
  x = 0
  while n % 2 !=0:
    n= int(input("Nhập lại: "))
  for i in range(n):
     if i % 2 == 0:
      x += i
  print(x)
Tongchan()