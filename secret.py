a=input("Enter the data:")
b=a.split(" ")
for i in b:
  m=i[1:len(i)]
  if len(i)>=3:
    j=i[0]
    k="lst"
    l="sat"
    print(k+m+j+l)
  elif len(i)==2:
    n=i[1]+i[0]
    print(n)
  else:
    print(i)