a = input("first name:")
b = input("last name:")
x = int(input("age:"))
c = int(input("date of birth (just year):"))

liste = [a,b,x,c]

for i in liste:
    if x < 18:
        print("first name: {}\nlast name: {}\nage: {}\ndate of birth: {}\nyou cant go out cos its dangerous".format(a,b,x,c))
    else:
        print("first name: {}\nlast name: {}\nage: {}\ndate of birth: {}\nyou can go out".format(a,b,x,c))
    break

