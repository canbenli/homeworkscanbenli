summ = 0
while summ < 5:
    while True:
        try:
            x = input("enter number that whatever you want: ")
            a = ("{}".format(float(x)))
        except ValueError:
            print("pls number!")
            continue
        if x == a:
            print("ur input is %s and it is a float." % (x))

        else:
            print("ur input is {} and it is an integer.".format(x))

        summ += 1
        break
