a=[1,2,3,4]
b = a
a.append(5)
print(b)
#-------------------------------------------------------
a=[1,2,3,4]
b = a.copy()
a.append(5)
print(b)
#---------------------------------------------------------
L1 = []
L1.append([1,[2,3], 4])
L1.extend([7,8,9])
print(L1[0][1][1] + L1[2])  # [[1,[2,3],4], 7,8,9]  3 + 8 = 11
#---------------------------------------------------------
D = {1:1,2 : '2', '1' :1, '2':3}
D['1'] = 2
print (D[D[D[str(D[1])]]])
#-------------------------------------------------------------
user_name = "joseph"
password = "w@12"
name = input("Please, enter a name : ")
if name == user_name :
    print("Hello ! {} the password is : {}" .format(user_name, password))
else :
    print("Hello ! {} see you later" .format(name))

