with open(r"first.txt", "r") as file:
    data=file.readlines()
    data[1]="This is true"
with open("first.txt", "w") as file:
    file.writelines(data)