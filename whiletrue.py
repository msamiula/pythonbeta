def table():
    while True:
        try:
            a = int(input("Enter number for Table: "))
            for i in range(1, 11):
                 print(f"{a} x {i} = {a * i}")
        except ValueError:
            print("Please enter a valid number!")
        finally:
             print("I hope you got it!")
    
table()