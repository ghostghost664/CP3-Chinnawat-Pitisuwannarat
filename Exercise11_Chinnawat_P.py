number = int(input("Fill the number"))
for i in range(number):
    text = ((2*i)*"*")+"*"
    print((" "*(number-i))+text)


