# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery

    def charge(self):
        return f"{self.model} is charging"

    def info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}mAh"

# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 5200)
phone2 = Smartphone("Samsung", "Galaxy S25", 512, 6500)
phone3 = Smartphone("Google", "Pixel 7", 128, 5000)
phone4 = Smartphone("Redmi", "15 Pro", 256, 5500)

print(phone1.info())
print(phone1.charge())
print(phone2.info())
print(phone2.charge())
print(phone3.info())
print(phone3.charge())
print(phone4.info())
print(phone4.charge())

