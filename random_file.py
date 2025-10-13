import random
import time
def sensor_data_stream():
    while True:
        yield {
            "heart_rate": random.randint(60,100),
            "Temperature" : round(random.uniform(97,0,100.0),1),
            "oxygen_level" : random.randint(90,100)
                    
            }
        time.sleep()
for reading in sensor_data_stream():
    print("Live Data: ", reading)
    