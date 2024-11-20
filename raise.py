a = input("Enter any value between 5 and 9. Write 'quit' to quit:")
def myfuc():
  if a=="quit":
    print("program quitted")
  elif:
    if(int(a)<5 or int(a)>9):
     raise ValueError("Value should be between 5 and 9")
    else:
      print(a)
myfuc()