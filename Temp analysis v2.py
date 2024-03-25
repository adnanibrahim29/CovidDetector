import pandas as pd

# Starting V2

with open('C:/Users/iadna/OneDrive/computer science/Leaving Cert Project/Temp_Readings.csv', 'r') as Data:
    Data = pd.read_csv('Temp_Readings.csv')
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    
    # Testing to print full data set
    print(Data)

    # Starting V3 
    
