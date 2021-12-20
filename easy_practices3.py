
phrase = "myemailaddress@clarusway.com"
print(len(phrase))
print(phrase.startswith("@", 14))
print(phrase.endswith(".", 15, 24))

source_string = "inteiroperyiabilitiymizyl"
print(source_string.strip("l"))

space_string = "      listen first      "
print(space_string.rstrip())  # removes spaces from the right side

print(not (None) or 5)

family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']
print(type(family_members))
family_members = tuple(['Meghan', 'Tom', 'Nicole', 'Tim'])
print(family_members)


print('www', 'clarusway', "com", sep='.', end=' ')
print('will', end=' ')
print('open', end=' ')
print('your', end=' ')
print('path', end='.')

print([] and ({0} or False))

var1 = "sleep"
var2 = "eat"
var3 = "better"
var4 = "life"
text = f"The less you {var1} and {var2}, the {var3} your {var4} will be."
print (text)




sentence = "I am 40 years old.{} I have two children. {} Data Science is my IT domain." .format("\n\t", "\n\t\t")
print(sentence)


student_ages = {"Harry": 29,
                "Clark": 32,
                "Peter": 22,
                "Bruce": 36
                }
print(student_ages["Clark"])


text = "Clarusway, Clarusway, Clarusway\n\tClarusway, Clarusway, Clarusway\n\t\tClarusway, Clarusway, Clarusway"
print(text)
print(len(set('listen to the voice of enlisted')))

flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
print(count1)

saved_amount = 99
ps4_price = 180
if saved_amount <= ps4_price/2 :
    print("You must save more, keep saving!")
if saved_amount >= ps4_price/2 :
    print("You saved more than half, keep saving!")
if saved_amount > ps4_price :
    print("Yippee! You can buy your PS4")


number = 23
if number >=10 :
    print("The number is equal or greater than 10")
elif number <= 10 :
    print("The number is less than 10")
else :
    print("The number is equal or less than 10")


math_mark = int(input('Please enter the mark: '))
if 100>= math_mark >=85  :
    print("A (Excellent)")
elif 70 <= math_mark <= 84 :
    print("B (Good)")
elif 60<= math_mark <=69 :
    print("C (Medium)")
elif 45<= math_mark <= 59 :
    print("D (not Bad)")
elif 0<= math_mark<=44 :
    print("F (Failed)")

#------------------------------------------
my_list=["a", "b", "c", "d", "e"]
a = 0
while a < len(my_list):
    print('square of {} is : {}'.format(a, a**2))
    a+=1

#----------------------------------------------
answer = 44
question = 'What number am I thinking of?  '
print ("Let's play the guessing game!")

while True :
    guess = int(input(question))

    if guess < answer:
        print('Little higher')
    elif guess > answer:
        print('Little lower')
    else:  # guess == answer
        print('Are you a MINDREADER!!!')
        break

#-----------------------------------------------------

flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0
while count1 > 0 :
    print(flowers[count2])
    count1 -= 1
    count2 += 1
#--------------------------------------------------------
iterable = [1, 2, 3, 4]
for i in iterable :
    print(i**2),  print(i+ i**2)
    i +=1

#----------------------------------------------------------
import random
print(random.random())
# --------------------------------
per_day, months = list(map(int, input().split()))

total_seconds = 21 * per_day * 30 * months
minutes = total_seconds // 60
seconds = total_seconds % 60
print("{} minutes and {} seconds".format(minutes,seconds))


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(5)
print('x is now', x)