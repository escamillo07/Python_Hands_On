vowels = "aeiou"
dict_vowel = {"a":1, "e":5, "i":9, "o":15, "u":21}
given_letter= input("Enter a lowercase letter : ")
def nearest_vowel(x) :
    if abs(given_letter - dict_vowel)

nearestwovel = (a, b,c,)

wovels = (a,e,ı,i,u,ü)

def nearestVowel(string) :
  vowel = "aeiou"
  order = [abs(ord(i) - ord(string)) for i in vowel]
  return vowel[order.index(min(order))]