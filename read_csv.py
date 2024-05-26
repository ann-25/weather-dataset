import pandas as pd

file_path = 'WeatherData.csv'

# Read the CSV file
df = pd.read_csv(r"C:\Users\Thomas\Desktop\weather dataset\WeatherData.csv") #add r to remove unicode

# Print the dataframe#
#print(df)

#Explore data

print(df.head()) # by default displays first 5 rows
print(df.tail()) # last rows
print(df.shape)  # shows number of rows and columns
print(df.index)
print(df.columns)
print(df.dtypes)
print(df.Temp_C .unique())
print(df.Weather.nunique())
print(df.nunique())
print(df.count())
print(df.Weather.value_counts)
print(df.info())

#all unique Wind Speed_km/h  
print(df['Wind Speed_km/h'].nunique())
print(df['Wind Speed_km/h'].unique())

#no. of times when the weather is clear
print(df.Weather.value_counts())   #values_counts
print(df[df['Weather'] == 'Clear'])   #filtering ;  two df is mentioned otherwise it will result boolean value
print(df.groupby('Weather').get_group('Clear')) #group by

#number of times the wind speed = 4km/h
print(df[df['Wind Speed_km/h' ]== 4])

#null values in the data
print(df.isnull().sum())  #using isnull command
print(df.notnull().sum()) 


#rename attribute name Weather  to Weather condition
print(df.rename(columns = {"Weather" : "Weather Condition"})) #column name is changed only for this command run. No change in data frame
print(df.rename(columns = {"Weather" : "Weather Condition"},inplace = True)) # to rename permanently
print(df.head(2))

#find mean visibility
print(df.Visibility_km.mean())

#standard deviation of pressure
print(df.Press_kPa.std())

#variance of relative humidity
print(df["Rel Hum_%"].var())

# all instanace when snow was founded

print(df["Weather Condition"].value_counts())   #values_counts
print(df[df['Weather Condition'] == 'Snow'])   #filtering
print(df.groupby('Weather Condition').get_group('Snow')) #group by
print(df[df["Weather Condition"].str.contains('Snow')])

# all instances when wind speed>24 and visibility = 25
print(df[(df["Wind Speed_km/h"] > 24)  & (df["Visibility_km"] == 25)])

#mean value of each clmn against "weather condition"
print(df.groupby('Weather Condition').mean())

#max and min value of each clmn against "weather condition"
print(df.groupby('Weather Condition').min() )
(df.groupby('Weather Condition').max()) 

#all records where weather conditions = fog
print(df[df['Weather Condition'] == 'Fog ']) 

# weather is clear and visibility > 40
print(df[(df["Weather Condition"] == 'Clear')  & (df["Visibility_km"] > 40)])

# all instances when weather is Clear and humidity > 50 or visibility > 40 
print(df[(df['Weather Condition'] == 'Clear') & (df["Rel Hum_%"] > 50) | (df["Visibility_km"] > 40) ]) 


