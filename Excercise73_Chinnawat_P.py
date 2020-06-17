menu1={"ข้าวไข่ข้น":35,"ข้าวไก่ย่างเทอริยากิ":45,"ยากิโซบะ":65,"ซาชิมิ":89}
menuList = []
print(menu1)

while True :
    menuName = input("please Enter to Menu")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,menu1[menuName]])

def showBill():
    print("-------MY FOOD-------")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        total += int(menuList[number][1])
    print('total price :',total)
showBill()
