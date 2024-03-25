import pandas as pd

with open('C:/Users/iadna/OneDrive/computer science/Leaving Cert Project/Project Code (Python)/Temp_Readings.csv', 'r') as Data:
    Data = pd.read_csv('Temp_Readings.csv')
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    

    # Printing Matching Columns for analysis
'''
    print(Data[['Times', 'Hot']])
    print1print(Data[['Times', 'Cold']])
    print(' ')
    
    print(Data[['Times', 'Room']])
    print(' ')
'''

    # Finding the Saturated water vapor in air
    # Converting C to Kelvin
    
Kelvin = 273

Hot_Kelvin = []
Cold_Kelvin = []
Room_Kelvin = []

Cold_Kelvin.append(Data['Cold']+ Kelvin)
Hot_Kelvin.append(Data['Hot']+ Kelvin)
Room_Kelvin.append(Data['Room']+ Kelvin)

#print(Hot_Kelvin)
#print(Cold_Kelvin)
#print(Room_Kelvin)

#print(' ')

# Finding the Saturated water vapor in air

Rv = 461
T = 273
e = 0.6113
L = 2.5*10**6

T_Hot = Data['HotK']
T_Cold = Data['ColdK']
T_Room = Data['RoomK']

# Formula = e * exp [L/Rv * (1/To - 1/T)]
# Kelvin subtraction (1/To - 1/T)

sub_hot = []
sub_cold = []
sub_room = []

sub_hot.append(1/T - 1/T_Hot)
sub_cold.append(1/T - 1/T_Cold)
sub_room.append(1/T - 1/T_Room)

def Saturated_Water_Vapor(x):
    # L/Rv
    fraction = []
    fraction.append(round(L/Rv))

    # fraction * sub
    import numpy as np

    # x = sub_hot, sub_cold, sub_room
    values = np.array(x)
    exponent = values * fraction
    
    #print("The exponent is: ", exponent)

    final_val = np.array(exponent)
    #print("The final val is: ", final_val)

    # Getting the exp
    # Finding the saturated water vaport in air

    Saturated_water_in_air = []
    Saturated_water_in_air.append(e * final_val)
    
    print("The Saturated water Vapor in air is: ", Saturated_water_in_air[-1][0])
    
    print(' ')
    
    return Saturated_water_in_air

    # https://geo.libretexts.org/Bookshelves/Meteorology/Book%3A_Practical_Meteorology_(Stull)/04%3A_Water_Vapor/4.00%3A_Vapor_Pressure_at_Saturation
    
    # Starting V6
    # Finding the Water vapor pressure
    # formula = simple_pressure = e^(20.386 - (5132 / (temperature + 273))

    # Kelvin Divison (5132 / (temperature + 273)

print(' ')

print("Room Saturated Water Vapor")
Room_Saturated = Saturated_Water_Vapor(sub_room)

print(' ')

print('Hot Saturated Water Vapor')
Hot_Saturated = Saturated_Water_Vapor(sub_hot)

print(' ')

print('Cold Saturated Water Vapor')
Cold_Saturated = Saturated_Water_Vapor(sub_cold)

Room_Saturated = Room_Saturated[-1][0]
Hot_Saturated = Hot_Saturated[-1][0]
Cold_Saturated = Cold_Saturated[-1][0]

# Uploading to firebase

from firebase import firebase

firebase = firebase.FirebaseApplication("https://lc-project-7eb68-default-rtdb.firebaseio.com/,", None)

counter = 0

for i in range(len(Room_Saturated)):
    data = {'Room': Room_Saturated[counter]}
    data2 = {'Hot': Hot_Saturated[counter]}
    data3 = {'Cold': Cold_Saturated[counter]}
    
    counter +=1
    
    firebase.post('/Room', data)
    firebase.post('/Hot', data2)
    firebase.post('/Cold', data3)

import pygal

line_chart = pygal.Line()
line_chart.title = 'Saturated Water Vapor in air'
line_chart.x_labels = map(str, range(0, 24))
line_chart.y_title = 'Saturated Water Vapor (mm)'
line_chart.x_title = 'Time (24h)'
line_chart.add('Room', Room_Saturated)
line_chart.add('Hot', Hot_Saturated)
line_chart.add('Cold', Cold_Saturated)
line_chart.render_to_file('C:/Users/iadna/OneDrive/computer science/Leaving Cert Project/Saturated Water Vapor graph.svg')
