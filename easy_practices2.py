
text = ['one','two','three','four','five','six']
numbers = [1, 2, 3, 4, 5,6,7]
for x, y in zip(text, numbers):
    print(x, ':', y)


#-----------------------------------------------

fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]
i = 0
output = []
for fruit in fruits:
 temp_qty = quantities[i]
 temp_price = prices[i]
 output.append((fruit, temp_qty, temp_price))
 i += 1
print(output)

#-------------------------------------------------
# FARKLARI GÖRMEK AÇISINDAN ANLAMLI GELDİ. ANCAK, İÇERİĞİ ANLAMLANDIRAMADIM.
liste1 = [1, 1, 2, 2, 1]
liste2 = ["a","a","b","b", "c"]   # output : {(2, 'b'), (1, 'a'), (1, 'c')}     NEDEN (2, 'b') en başta .
print(set(zip(liste1, liste2)))   # set sayıları rastgele sıralar kuralından mı kaynaklı?

liste1 = [1, 1, 2, 2, 1]
liste2 = ["a","a","b","b", "c"]    # output : {1: 'c', 2: 'b'} sıralama ilginç degil mi? SAYILARI LİSTE 2 NİN
print(dict(zip(liste1, liste2)))   # SONUNDAN ALIYOR.EGER SONDA 1 YERİNE 3 KOYARSAM SONUÇ:{1: 'a', 2: 'b', 3: 'c'}

liste1 = [1, 1, 2, 2, 1]     # bunda sıkıntı yok.
liste2 = ["a","a","b","b", "c"]
print(tuple(zip(liste1, liste2)))  #output: ((1, 'a'), (1, 'a'), (2, 'b'), (2, 'b'), (1, 'c'))

#-------------------------------------------------
bool_value =False
if bool_value :
     print("Yes")
else :
    print("No")

#----------------------------------------------------
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#-------------------------------------------------------


#--------------------------------------------------------
sentence = input("Enter a sentence: ")
counter =0
for i in sentence :
    counter +=1
    print(i, end="-")

per_day, months = list(map(int, input().split()))

total_seconds = 21 * per_day * 30 * months
minutes = total_seconds // 60
seconds = total_seconds % 60
print("{} minutes and {} seconds".format(minutes,seconds))