# Building a Calculator using dict with lambda experession
# beginner lar için "dict" hesap makinesi yapımında kullanmak ilginç geliyor.halbuki dict bize bu konuda cok büyük kolaylıklar sunuyor.
# basit tımer lı fırın ocak çamaşır mak. gibi aletlerin calculator ları bu mantıkla yapılabiliyor. Ayrıca: key:value kombinasyonu ve bunların
# birbiriyle çağrılabilmesi süper olanaklar sunuyor. sayılara, isimlere, kişilere, makielere, vb. karşılığında sayı atayıp
# aritmatik işlemler yapabiliyorum.
#-------------------------------örnek soru---------------
calculator =  { "+" :(lambda x,y : x+y), # tüm yaptığımız key ve value değer tanımlamak oldu. ancak lambda yı burada value
# olarak tanımlayıp işlem yaptırmak harika birşey oldu. Bu mantığı geliştirerek çok şey yapılabilir. aklıma geldiği kadarıyla,
# Bir öğrenci isim listesi düşünün. value bölümünde, herkesin tüm notlarını vb. hemen karşısında hesaplayan bir program yapabilirim.
                "-" :(lambda x,y : x-y),
                "*" :(lambda x,y : x*y),
                "/" :(lambda x,y : x/y)}

print(calculator["+"](12,68))