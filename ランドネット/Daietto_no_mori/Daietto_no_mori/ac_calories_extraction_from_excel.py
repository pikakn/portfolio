import pandas as pd

def return_oneweek_ac_calories():
    df = pd.read_excel('datafile/home_data.xlsx', sheet_name='Sheet1')

    calorie_list = df['累計カロリー'].dropna().tail(7).tolist()
    
    return sum(calorie_list)

print(return_oneweek_ac_calories())