#BT3
sum = 0
n = int(input('nhap n: '))

while(n>999 or n < 0):
    n = int(input( print('nhap lại ! lưu ý nhập các số bé hơn 1000: ')))
if n<1000:
    for i in range(1,n+1):
        sum = sum+i
        print("tong : "+str(sum))
