
    
def odd_even(x):
    try:
        print(f"{x}   is a Even" if x % 2 ==0 else f"{x}  is a Odd")
        
    except Exception as e:
        print(f"it is not valid {e}")

for num in range(25):
    odd_even(num)
  