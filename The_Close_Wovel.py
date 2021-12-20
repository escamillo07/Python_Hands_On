
letters = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
dic = {}
def nearest_Vowel(char):

  for i in vowels:
      dic[i] =abs(letters.index(i) - letters.index(char))
  return min(dic, key=dic.get)

nearest_Vowel('m')


















