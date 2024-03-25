import serial
import time

# Microbit info

ser = serial.Serial()
ser.baudrate = 115200

ser.port = 'COM4'

ser.open()

Repeat_Times = 0

# 24 times = every hour the temp gets recorded
# Reapting x amount of times

while Repeat_Times < 24:
    Values = str(ser.readline())
    
    print(" ")
    
    # Time delay time frame
    
    time.sleep(2)
    
    Repeat_Times = Repeat_Times +1
    
    # Cleaning the importing data
    
    Values = Values.replace("b", " ")
    Values = Values.replace("'", " ")
    Values = Values.replace("\\r\\n", " ")
    Values = Values.replace("Room:", " ")
    
    # Sending data to a CSV file
    
    if Values is not None:
        with open("C:/Users/iadna/OneDrive/computer science/Leaving Cert Project/Temp_Readings_v4.csv", "a") as TempValues:
            TempValues.write(Values + "\n")
            
    print(Values)
    