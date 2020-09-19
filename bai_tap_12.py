# BT12: viết chương trình nhập một số gồm hai chữ số in ra màn hình số hàng đơn vị và số hàng chục 
"""code"""

a = int(input('Nhập vào'))
dv = a%10
Hangchuc = a//10
print("Số hàng đơn vị là ",dv,"\n số hàng chục là",Hangchuc)
