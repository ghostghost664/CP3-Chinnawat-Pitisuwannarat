from tkinter import*

import math

def BMIresult() :
    result = math.ceil(float(TextboxWeight.get()) / math.pow(float(TextboxHeight.get()) / 100, 2))
    if result > 30 :
        Text1Label = Label(main)
        Text1Label.grid(row=3, column=1)
        Text1Label.configure(text="อ้วนมาก!! X(",font = 52)
        print("อ้วนมาก!! X(")
    elif 25 < result <29.9 :
        Text2Label = Label(main)
        Text2Label.grid(row=3, column=1)
        Text4Label.configure(text="อ้วน! +.+",font = 42)
        print("อ้วน! +.+")
    elif 23 < result <24.9 :
        Text3Label = Label(main)
        Text3Label.grid(row=3, column=1)
        Text3Label.configure(text="น้ำหนักเกิน :P",font = 26)
        print("น้ำหนักเกิน :P")
    elif 18.6 < result <22.9 :
        Text4Label = Label(main)
        Text4Label.grid(row=3, column=1)
        Text4Label.configure(text="น้ำหนักปกติ :)")
        print("น้ำหนักปกติ :)")
    elif result<18.5 :
        Text5Label = Label(main)
        Text5Label.grid(row=3, column=1)
        Text5Label.configure(text="ผอมเกินไป :o")
        print("ผอมเกินไป :o")
def Leftclickbutton(event):
    result = math.ceil(float(TextboxWeight.get())/math.pow(float(TextboxHeight.get())/100,2))
    print(result)
    ResultLabel.configure(text=result)
    BMIresult()

main = Tk()
HeightLabel = Label(main,text ="ส่วนสูง(cm.)").grid(row=0,column=0)
TextboxHeight = Entry(main)
TextboxHeight.grid(row=0,column=1)
WeightLabel = Label(main,text ="น้ำหนัก(kg.)").grid(row=1,column=0)
TextboxWeight = Entry(main)
TextboxWeight.grid(row=1,column=1)





CalculationButton = Button(main,text="คำนวณBMI")
CalculationButton.bind('<Button-1>',Leftclickbutton)
CalculationButton.grid(row=2)

ResultLabel = Label(main,text ="ค่า BMI")
ResultLabel.grid(row=2,column=1)


main.mainloop()

