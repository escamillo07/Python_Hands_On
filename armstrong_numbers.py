# armstrong numbers
num = (input("Enter a number : "))
if number< 0 :
  print("{} is a negative number".format(num))
elif number == float :
  print("{} is a float number".format(num))
elif number== "str" :
  print("{} is a string number".format(num))
else :
    continue
toplam = sum([int(i) ** len(num) for i in num])
if int(num) == toplam :
  print(num, "is a armstrong number")
else:
  print(num, "is not a armstrong number")