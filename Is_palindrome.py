def is_palindrome(string):
   return string[::-1].casefold() == string.casefold() # düzden ve tersten yazılışının aynı olmasını birbirine eşitledim.


def palindrome_sentence(sentence):    # sentence parametreli bir fonksiyon tanımlandı.
    string = ""                       # boş bir string "kutusu" koydum. Birazdan testten geçenler buraya yazılsın diye...
    for char in sentence:             # for ile sentence içindeki karaekterleri tek tek inceleyeceğim.
        if char.isalnum():            # Fakatttt, alfanumerik olmıyanları ayıklamam lazım. ?,?*-% vs. tertemiz olmalı.
            string += char            # testen geçenleri yukarıya" string kutusuna"  gönderiyorum.
    print(string)                     # şimdi string'i yazdırıyorum.. yanyana ayıklanmış bir vaziyette. eğer bunu silersem bu kısım görünmez o kadar. çok lazım değil.
    return is_palindrome(string)      # DİKKAT!!!!STRİNG TESTİ BİTİNCE BU FONKSİYONDAN BAŞTAKİ FONKSİYONA GİDİYOR. KARŞILAŞTIRMA YAPSIN DİYE.

word = input("Please enter a word to check: ")    # Şimdi girilen kelime değişkene atanıyor.
if palindrome_sentence(word):                     # bu satır diyor ki: ey!! palindrome_sentence! fonksiyonu sana bir argument gönderiyorum. Şunu bir test bakalım....esasında ilk start buradan verilmiş oluyor
    print("'{}' is a palindrome".format(word)) # f-string le süslenerek servis ediliyor.
else:
    print("'{}' is not a palindrome".format(word))