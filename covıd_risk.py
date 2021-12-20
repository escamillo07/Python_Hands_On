
numbers = int(input("Enter seven numbers: "))
numbers_list = list(numbers)
max_number = numbers_list.sort()
print(max_number[6])

print(format("Welcome", "10s"), end = '#')
print(format(111, "4d"), end = '#')
print(format(924.656, "3.2f"))



# odev github a gönderilecek....
age = input("are you older than 75 years old")
chronic = input("do you have cigarette disease?")
immune = input("is your immune system too weak")
if age=="yes" and chronic == "yes" and immune == "yes" :
    print ("you are in risky group")
else:
    print("you are not in risky group")


age = input("Are you a cigarette addict older than 75 years old?(Yes or No): ").lower()
chronic = input("Do you have a severe chronic disease?(Yes or No): ").lower()
immune = input("Is your immune system too weak?(Yes or No): ").lower()
if (age == "yes" or chronic == "yes" or immune == "yes"):
    print("You are in risky group")
else:
    print("You are not in risky group")




















