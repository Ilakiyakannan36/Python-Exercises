# Parent class 
class MedicalDevice: 
    def __init__(self, device_name): 
        self.device_name = device_name 
 
    def switch_on(self): 
        print(f"{self.device_name} is now switched on.") 
         
# Child class inherits from MedicalDevice 
class HeartMonitor(MedicalDevice): 
    def display_heart_rate(self, bpm): 
        print(f"Heart rate: {bpm} bpm") 
 
class AdvancedHeartMonitor(HeartMonitor): 
    def alert_irregular_heartbeat(self): 
        print(f"{self.device_name} alerts: Irregular heartbeat detected!") 
 
class DeviceNetwork: 
    def connect_network(self): 
        print("Device connected to hospital network.") 
 
class SmartMedicalDevice(HeartMonitor, DeviceNetwork): 
    def auto_update(self): 
        print(f"{self.device_name} software updated automatically.") 
 
class BloodPressureMonitor(MedicalDevice): 
    def display_bp(self, systolic, diastolic): 
        print(f"Blood Pressure: {systolic}/{diastolic} mmHg") 
class SmartAdvancedMonitor(SmartMedicalDevice, AdvancedHeartMonitor): 
    def remote_monitoring(self): 
        print(f"{self.device_name} is now available for remote monitoring.") 
# Usage 
sam = SmartAdvancedMonitor("NextGen ECG Monitor") 
sam.switch_on()             
# From MedicalDevice 
sam.display_heart_rate(78)  # From HeartMonitor 
sam.connect_network()       
# From DeviceNetwork 
sam.alert_irregular_heartbeat() # From AdvancedHeartMonitor 
sam.remote_monitoring()     # Own method