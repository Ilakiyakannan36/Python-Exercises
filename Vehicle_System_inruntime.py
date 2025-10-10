class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def accept(self):
        brand= input("Enter brand name : ")
        model= input("Enter model name : ")
    def start(self):
        print(f"{self.brand} {self.model} is starting")

class  car(vehicle):
    def play_music(self):
        print(f"{self.brand} {self.model} music is playing")

class electric_vehicle(car):
    def charge(self):
        print(f"{self.brand} {self.model} is charging")

class smart_device:
    def __init__(self,wifi):
        self.wifi=wifi
    def connect_wifi(self):
        print(f"{self.brand} {self.model} is connected to wifi")

class smart_car(car, smart_device):
    def auto_drive(self):
        print(f"{self.brand} {self.model} auto driving mode is on")

class bike(vehicle):
    def kick_start(self):
        print(f"{self.brand} {self.model} is kick started")

class electric_smartcar(smart_car, electric_vehicle):
    def autopilot_mode(self):
        print(f"{self.brand} {self.model} is on auto pilot mode")
print("****** Car Details*******")

def vehicle_system():
    while True:
        print("\n***** Vehicle System *****")
        print("1. Vehicle")
        print("2. Car")
        print("3. Electric Vehicle")
        print("4. Smart Car")
        print("5. Bike")
        print("6. Electric Smart Car")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            v = vehicle("", "")
            v.accept()
            v.start()

        elif choice == "2":
            c = car("", "")
            c.accept()
            c.start()
            c.play_music()

        elif choice == "3":
            ev = electric_vehicle("", "")
            ev.accept()
            ev.start()
            ev.play_music()
            ev.charge()

        elif choice == "4":
            sc = smart_car("", "")
            sc.accept()
            sc.start()
            sc.connect_wifi()
            sc.auto_drive()

        elif choice == "5":
            b = bike("", "")
            b.accept()
            b.start()
            b.kick_start()

        elif choice == "6":
            esc = electric_smartcar("", "")
            esc.accept()
            esc.start()
            esc.play_music()
            esc.connect_wifi()
            esc.charge()
            esc.autopilot_mode()

        elif choice == "7":
            print("Exiting Vehicle System. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


vehicle_system()