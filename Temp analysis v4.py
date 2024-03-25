import pandas as pd
from csv import writer

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

# Starting V5


    