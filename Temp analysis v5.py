import pandas as pd

# Starting V2

with open('C:/Users/iadna/OneDrive/computer science/Leaving Cert Project/Temp_Readings.csv', 'r') as Data:
    Data = pd.read_csv('Temp_Readings.csv')
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    
    # Starting V3
    # Printing Matching Columns for analysis
'''
    print(Data[['Times', 'Hot']])
    print(' ')
    
    print(Data[['Times', 'Cold']])
    print(' ')
    
    print(Data[['Times', 'Room']])
    print(' ')'''

    # Starting V4
    # Finding the Saturated water vapor in air
    # Converting C to Kelvin
    
Kelvin = 273

Hot_Kelvin = []
Cold_Kelvin = []
Room_Kelvin = []

Cold_Kelvin.append(Data['Cold']+ Kelvin)
Hot_Kelvin.append(Data['Hot']+ Kelvin)
Room_Kelvin.append(Data['Room']+ Kelvin)
print(Hot_Kelvin)
print(Cold_Kelvin)
print(Room_Kelvin)

print(' ')

# Starting V5
# Finding the Saturated water vapor in air

Rv = 461
T = 273
e = 0.6113
L = 2.5*10**6
T_Hot = Data['HotK']
T_Cold = Data['ColdK']
T_Room = Data['RoomK']

import math

# Formula = e * exp [L/Rv * (1/To - 1/T)]
# Kelvin subtraction (1/To - 1/T)
sub_hot = []
sub_cold = []
sub_room = []

sub_hot.append(1/T - 1/T_Hot)
sub_cold.append(1/T - 1/T_Cold)
sub_room.append(1/T - 1/T_Room)

def Temps(x):
    # L/Rv
    fraction = []
    fraction.append(round(L/Rv))

    print(' ')

# fraction * sub
    import numpy as np

    values = np.array(x)
    exponent = values * fraction
    print("The exponent is: ", exponent)

    print(' ')

    final_val = np.exp(exponent)
    print("The final val is: ", final_val)

    print(' ')

# Getting the exp
# Finding the saturated water vaport in air

    Saturated_water_in_air = []
    Saturated_water_in_air.append(e * final_val)
    print("The Saturated water Vapor in air is: ", Saturated_water_in_air)

    print(' ')

Temps(sub_hot)
Temps(sub_cold)
Temps(sub_room)


