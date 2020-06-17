menuList = []

def showBill():
    total = 0
    print("-------MY FOOD-------")
    for number in range(len(menuList)):
        print(menuList[number])
        total += int(menuList[number][1])
    print('total :', total)
while True :
    menuName = input("please Enter to Menu")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])

print(menuList)
showBill()
