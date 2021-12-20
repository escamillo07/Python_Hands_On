sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],           # bu diziye böyle alt alta yazdırması olayın %50 sini çözmüş gibi geldi bana.daha rahat düşünebildim doğrusu. cevap olmasa cok da düşünemezdim doğrusu.
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

# --------------------------------------------- #

count = 0                                 # sayacı sıfırlıyoruz. neden? yaptığım işlemi sayacağım. sonrasında ----- çekicem. kaç seferde bir çizgi çeksin.3 satır işlem 4'te çizgi...
print('- ' * 15)                          # ilk çizgiyi ben çekiyorum manuel olarak....
for i in sudoku:                          # sudokunun ilk satırını tek tek alıyor j indexinin(kutulara yerleştir anlamında) içine yerleştiriyor.
    for j in range(9):                    # 0'dan sekize kadar 9 kutu oluştur diyor.
        print(i[j], " ", end="")          # herbir i karakterini j kutusuna yaz, aralarına boşluk koy.(end= " " komutu ile de, alt alta yazdırma yanyana yazdır diyor. yoksa alt alta yazılır. default
        if j == 8 :                       # j 8 olunca malum 9 karakter olmuş olacak. eee ne olacak?????
            print()                       # print seni alta indirsin ve bir satır da boşluk koysun diyor.geçen bu konuyu tartıştık..
            count+=1                      # count :bu mantığı seviyorum ben. Bunu içselleştirmek lazım.Sayaç kullanabilmeyi. işlemimi say ve 3 işlemden sonra bana birşey yap diyecek.
            if count%3==0  :              # 3 olunca modulus 0 olacak malum ve count tabiki 0 olmayacak(bunu yazmasam ne olur kiiii. ) 3 6 ve 9 sonunda  ----- çek diyor.
                print("- - - - - - - - - - - - - - - ") # bunu yarım otomatik yapıyor diyebiliriz sanırım. bu da bodoslama ------  malum.
        if (j+1) % 3 == 0 and  j !=8:   # sen alt alta yaptın bunu kolaydı. hadi birde yan yana yani dikey yap bakalım diyor.
             print("| ", end="")            # oooo cok güzel bir mantık daha var burada yaaaa.Dananın kuyruğunun koptuğu yer burası gibi geldi bana amaaa sizi bilemem.
                                            # if diyorki : dikey 2. index'e  +1 ekle  3 olsun modulus  0 olur. bu bu 2 ve 5 de tekrarlasın ama 0 ve 8'de olmasın .neden?
                                            # çünkü 0 da 8 de dikey çizgi istemiyorum. o yüzden boolean (and) kullanmış her iki if blogunda....yana boşluk koymayı da unutmamışş. (end= "")