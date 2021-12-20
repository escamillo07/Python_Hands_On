a = set('abracadabra')
b = set('alacazam')
print(a - b)  # same as '.difference()' method
print(a.difference(b)) # a difference from b

s = set('unselfishness')
print(s)

dict_by_dict = {'animal': 'dog', 'planet': 'neptun', 'number': 40, 'pi': 3.14, 'is_good': True}
print(dict_by_dict.items(), '\n')
print(dict_by_dict.keys(), '\n')
print(dict_by_dict.values(), '\n')

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # BİRİNCİ KARAKTERİ SİLDİK
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

x = 60
y = 6
z = 10
z = y
y = x
x = z
print(x, y, z, sep="-")
print(len([[12, 34, 56]][0]))
print("{9} {7} {1} {10} {3} {2} {5} {8} {6} {0} {4}".format('in', 'know', 'bring', 'to', 'students.', 'out', 'best',
                                                            'teachers', 'the', 'Good', 'how'))

name = "JOSEPH"
job = "teachers"
domain = "Data Science"
message = (f"Hi {name}. "
           f"You are one of the {job} "
           f"in the {domain} section.")
print(message)

text = 'Sana dün bir tepeden baktım ey aziz istanbul'
print(text.endswith('bul'))
print(text.startswith('http:'))
print(text.startswith('Sana'))






















