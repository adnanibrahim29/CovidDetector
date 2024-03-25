import pandas as pd

# Starting V2
with open('C:/Users/iadna/OneDrive/computer science/Leaving Cert Project/Temp_Readings.csv', 'r') as Data:
    Data = pd.read_csv('Temp_Readings.csv')
    pd.set_option("display.max_rows", None, "display.max_columns", None)

    # Starting V3
    # Testing to print matching columns for analysis
    
    print(Data[['Times', 'Hot']])
    print(' ')
    
    print(Data[['Times', 'Cold']])
    print(' ')
    
    print(Data[['Times', 'Room']])
    print(' ')
    
    # Starting V4
    