menuList = []
priceList = []

def showBill():
    total = 0
    print("-------MY FOOD-------")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        total += int(priceList[number])
    print('total :', total)
while True :
    menuName = input("please Enter to Menu")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
