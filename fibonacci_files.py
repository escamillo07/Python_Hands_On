ilk_sayi = 0
son_sayi = 1
fibo_list =[]
while son_sayi <= 55:
  fibo_list.append(son_sayi)
  ilk_sayi, son_sayi = son_sayi, son_sayi + ilk_sayi  # easy, simple and brillant. thanks to gulcan.
print(fibo_list[:])
#-----------------------------------------
fibo_list = [0,1]
for i in range(1,10):
  i = fibo_list[i] + fibo_list[i-1]
  fibo_list.append(i)
  if i == 55:
    break
print(fibo_list[1:])
#------------------------------------
ilk_sayi = 0
son_sayi = 1
gecici_sayi = 1
fibo_list =[]
son_deger = input("Liste hangi sayıya kadar olsun?")
while son_sayi <= int(son_deger):
  fibo_list.append(son_sayi)
  gecici_sayi = son_sayi + ilk_sayi
  ilk_sayi = son_sayi
  son_sayi = gecici_sayi
print(fibo_list[:])




