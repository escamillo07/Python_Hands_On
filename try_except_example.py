counter = 3
while counter > 0 :
    fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
    try :
        print(f"you have {counter} right.")
        index = int(input("pick an index number."))
        print("your favorite fruit is", fruits[index])

    except IndexError :
        counter -=1
        print(f"Index error. You have {counter} right left. Try again!")

    except  ValueError :
        counter -= 1
        print (f"Value error. You have {counter} right left. Try again!")

    else :
        print("congrats! You have entered valid input.")
        break

    finally:
        print("Our fruits are always fresh!!!!!.just taste it.!")


