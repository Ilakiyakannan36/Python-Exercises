class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def accept(self):
        brand= input("Enter brand name : ")
        model= input("Enter model name")
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
brand=input("Enter Brand name :  ")
model=input("Enter Model Name : ")
#vehicle
v=vehicle("Hyundai", "Venue")
v.start()
print()
#car
c = car("Toyota", "Corolla")
c.start()
c.play_music()
print()

# Electric Vehicle
ev = electric_vehicle("Tata", "Nexon")
ev.start()
ev.charge()
print()

# Smart Car
sc = smart_car("Tata", "Nano")
sc.start()
sc.connect_wifi()
sc.auto_drive()
print()

# Bike
b =bike("Yamaha", "R15")
b.start()
b.kick_start()
print()

# Electric Smart Car
esc = electric_smartcar("EV", "Comet")
esc.start()
esc.play_music()
esc.connect_wifi()
esc.charge()
esc.autopilot_mode()
