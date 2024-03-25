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
    print(' ')
'''

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

#print(Hot_Kelvin)
#print(Cold_Kelvin)
#print(Room_Kelvin)

#print(' ')

# Starting V5
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

    values = np.array(x)
    exponent = values * fraction
    #print("The exponent is: ", exponent)

    final_val = np.exp(exponent)
    #print("The final val is: ", final_val)

    # Getting the exp
    # Finding the saturated water vaport in air

    Saturated_water_in_air = []
    Saturated_water_in_air.append(e * final_val)
    print("The Saturated water Vapor in air is: ", Saturated_water_in_air)
    
    print(' ')

    # https://geo.libretexts.org/Bookshelves/Meteorology/Book%3A_Practical_Meteorology_(Stull)/04%3A_Water_Vapor/4.00%3A_Vapor_Pressure_at_Saturation
    
    # Starting V6
    # Finding the Water vapor pressure
    # formula = simple_pressure = e^(20.386 - (5132 / (temperature + 273))

    # Kelvin Divison (5132 / (temperature + 273)

    def Water_Vapor_Pressure(y):
    
        import numpy as np
    
        Heat_vapor = 5132

        Hot_vals = np.array(y)
        Final_Heat_Val = Heat_vapor / Hot_vals
        #print("The final Heat val is:", Final_Heat_Val)
        # Finding the water vapor pressure

        S_Heat = 20.386
        Water_Pressure = S_Heat - Final_Heat_Val
        print("The Water Vapor Pressure is: ", Water_Pressure)

        print(' ')
        
        # https://www.omnicalculator.com/chemistry/vapour-pressure-of-water#:~:text=Simple%20formula,mmHg%20and%20temperature%20in%20kelvins.

        # Finding the relative humidity
        # formula = actual water vapor pressure / saturated water vapor pressure * 100

        # RH = Relative humidity
            
        RH_actual = np.array(Water_Pressure)
        RH_saturated = np.array(Saturated_water_in_air)
            
        RH_Div_Vals = RH_actual / RH_saturated

        RH = RH_Div_Vals * 100

        print("The Relative humidity is: ", RH)
        
        # https://www.engineeringtoolbox.com/relative-humidity-air-d_687.html
        
        print(' ')
    
    print("Hot")
    Water_Vapor_Pressure(Hot_Kelvin)
    
    print(' ')
    
    print("Cold")
    Water_Vapor_Pressure(Cold_Kelvin)
    
    print(' ')
    
    print("Room")
    Water_Vapor_Pressure(Room_Kelvin)
    
    print(' ')

print("Hot")
Saturated_Water_Vapor(sub_hot)

print(' ')

print("Cold")
Saturated_Water_Vapor(sub_cold)

print(' ')

print("Room")
Saturated_Water_Vapor(sub_room)

# Starting V7
# Uploading to firebase





    
    


