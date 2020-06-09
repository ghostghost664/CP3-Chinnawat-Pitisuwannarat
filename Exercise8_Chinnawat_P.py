usernameInput = input("Usename : ")
passwordInput = input("Password : ")
if usernameInput == "Chinnawat" and passwordInput == "1234":
    print("Welcome to MyShop101")
    print("--------MyShop101--------")
    print("1.Banana 10 THB/piece")
    print("2.Orange 20 THB/piece")
    print("3.Papaya 30 THB/piece")
    userSelected = int(input("Add to cart (fill the number1-3)>>"))
    Quantity = int(input("Quantity x "))
    if userSelected == 1 :
        price1 = 10
        vat = 7
        result1 = int((((price1)*vat/100)+int(price1))*Quantity)
        print("Total price including VAT",result1)
    elif userSelected ==2 :
        price2 = 20
        vat = 7
        result2 = int((((price2)*vat/100)+int(price2))*Quantity)
        print("Total price including VAT",result2)
    elif userSelected == 3:
        price3 = 30
        vat = 7
        result3 = int((((price3)*vat/100)+int(price3))*Quantity)
        print("Total price including VAT",result3)

else:
    print("Username or Password Incorrect")