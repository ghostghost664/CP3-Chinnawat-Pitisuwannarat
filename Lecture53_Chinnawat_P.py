def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return(int(result))

print(vatCalculate(int(input("Fill your Price"))))