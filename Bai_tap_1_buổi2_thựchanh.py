#BT1 Xuất ra màn hình N lần câu thông báo “Hello Python”
#Gợi ý: dùng vòng lặp cho chạy từ i đến N, trong thân vòng lặp gọi lệnh print (“Hello Python”)
"""code"""
"""
for i in range(1,7,1):
  print('hellworld python')
"""
#BT2: Tính tổng từ 1 cho đến N
"""code"""
"""
sum = 0
n = int(input('nhap n: '))
for i in range(1,n+1):
  sum = sum+i
print("tong : "+str(sum))
"""
#BT3: Tính tổng các số CHẴN nằm trong đoạn từ 0 đến N
"""code"""
"""
sum = 0
n = int(input('nhap n'))
for i in range(1,n+1):
  if i%2==0:
    sum = sum+i
    print("tong : "+str(sum))
"""
#BT4: Tính tổng các số LẼ nằm trong đoạn từ 0 đến N
"""code"""
"""
sum = 0
n = int(input('nhap n'))
for i in range(1,n+1):
  if i%2 not 0:
    sum = sum+i
    print("tong : "+str(sum))
    """
#BT5: Tính trung bình cộng các số trong mảng
"""code"""
"""
tong = 0
n = int(input('Nhập n: '))
for i in range(1,n+1):
  tong = tong + i
  print(i,end=' ')
print('tbc:',tong/n)
"""
#BT6: Tính tổng giá trị từ 1 đến N, nếu chạy đến số 13 thì không chạy nữa và xuất kết quả
""" code """

tong = 0
n = int(input('Nhập n : '))
for i in range(1,n+1):
  if(i == 14):
    break
  tong = tong + i
  print(i)
print('tong: '+ str(tong))
 
 #BT7: Tính tổng giá trị từ 1 đến N, riêng số 17 thì bỏ qua
""" code """
"""
tong = 0
n = int(input('Nhập n : '))
for i in range(1,n+1):
  if(i == 17):
   continue
  tong = tong + i
  print(i)
print('tong: '+ str(tong))
"""
