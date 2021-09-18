import pandas as pd

col_list = ['order_amount']
df = pd.read_csv("/Users/Clara/csv/CDS.csv", usecols=col_list)
print(df) #for reference
print(df.median()) #find median of order amounts
df2 = df.sort_values(by=col_list, ascending=False) #sort order amounts descending
print(df2) #to confirm sorted
print(df2.iloc[:2500].median()) #find upper quartile
print(df2.iloc[2500:].median()) #find lower quartile

#using printed quartiles, calculate outlier range and max acceptable value (730.5)

#use for loop to keep only non-outliers
sum = 0 #where non-outliers will be stored
count = 0 #where the number of non-outliers will be stored

for i in range(5000):
    value = df['order_amount'][i]
    if(value <= 730.5): #calculated max acceptable value from IQRs*1.5
        sum += value
        count +=1
print(sum/count) #calculate average without outliers
