try :
    x=3/0
    print("evrything is Ok.")   # not: bir programda çalışırken aralarda yaptığım hataları bana göstersin istiyorsun.
except:                         # Muhtemel hataları except ile yazdırıyorsun. hatalarına tedbir alıyorsun.
    print("something went wrong") # burada ne hatası yapılabilirimi öngörüp ismini de yazabilirsin. genel anlamda da yazabilirsin.
else :                          # örneğin; value error, name error, zerodivision error gibi. Bu hataların uzun bir listesi var.
    print("nasılsın")           # zamanla pekiştirilecek bir konu. kafa yemeye gerek yok.
finally:                        # else try ın kardeşi. try çalışırsa else de ben de çalışırım diyor. bir sey yazıyor işte.
    print("always execute this") #finanly hepsinin emmi oğlu. ikisinde de except ve try dahil calışıyor ve birşey yazdırıyor.
                     # tüm olay budur. ben adım hıdır.
# examples

try :
    x= 2/0
except ZeroDivisionError :
    print("attempt to divide by zero")  #attempt to divide by zero  verir.
except :
    print("something went wrong")

# examples
try :
    x
except ZeroDivisionError :
    print("attemp to divide by zero")
except NameError :
    print("act accordance with name error")
except :
    print("something else went wrong")   # act accordance with name error   verir

# examples
try :
    int("on")
except ZeroDivisionError :
    print("attemp to divide by zero")
except NameError :
    print("act accordance with name error")
except :
    print("something else went wrong")   # something else went wrong   verir. neden? çünkü bu value error.


# examples


