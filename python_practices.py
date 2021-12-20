my_list = list(range(11))
new_list = sorted(my_list, reverse=True)
print(new_list)

grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
print(grocer[1][1][1:6:2])

flowers = [["jasmine", ["lavender", "rose"], "tulip"]]  # bu soruyu bulmak için canım çıktı.
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
text = f"My favorite flowers are {flowers[0][2]} and {flowers[0][1][1]}, two favorite colors are {colors[1][0]} and {colors[1][1][1]}."
print(text)
text = "My favorite flowers are {} and {}, two favorite colors are {} and {}.". format(flowers[0][2], flowers[0][1][1], colors[1][0], colors[1][1][1])
print(text)

# odev github a gönderilecek....
age = input("are you older than 75 years old")
chronic = input("do you have cigarette disease?")
immune = input("is your immune system too weak")
if age=="yes" and chronic == "yes" and immune == "yes" :
    print ("you are in risky group")
else:y
    print("you are not in risky group")


age = input("Are you a cigarette addict older than 75 years old?(Yes or No): ").lower()
chronic = input("Do you have a severe chronic disease?(Yes or No): ").lower()
immune = input("Is your immune system too weak?(Yes or No): ").lower()
if (age == "yes" or chronic == "yes" or immune == "yes"):
    print("You are in risky group")
else:
    print("You are not in risky group")