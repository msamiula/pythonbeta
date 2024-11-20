a=int(input("enter first number between (1-5)"))
match a:
    case 0:
        print("Cannot Process")
    case _ if a > 5:
        print("Cannot Process")
    case _:
        print("Your Lucky Number is", a*7)
    

