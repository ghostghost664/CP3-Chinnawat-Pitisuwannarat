def login():
    usernameInput = input("Usename : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("LOGIN SUCCESS")
        return True
    else:
        print("Username or Password incorrect")
def showMenu():
    print("--------iSHOP--------")
    print("1.Vat Calculator")
    print("2.Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        VatCalculate(int(input("Price..")))
    elif userSelected == 2 :
        PriceCalculate()
def VatCalculate(totalprice):
    vat = 7
    result = (totalprice * vat / 100) +totalprice
    print(result)
    return result
def PriceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return VatCalculate(price1 + price2)

login()
showMenu()
menuSelect()
