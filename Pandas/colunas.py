import pandas as pd

df = pd.read_csv('Electric_Vehicle_Population_Data.csv')

data =  pd.DataFrame(df,columns= ['City', 'State'])

print(data.head(5))	

print(data.tail(5))
