print("welcome to ATM")
correct_pin = "7805"
while True:
    pin=input("enter the pin=")
    if pin== correct_pin:
        print("pin valid")
        break
    else:
        print("pin invalid")
