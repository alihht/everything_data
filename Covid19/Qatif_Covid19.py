import csv
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib.pyplot as plt

path = 'C:\\Users\\alihh\\everything_data\\Covid19\\'

file=open( path +"Qatif_data.csv", "r")
reader = csv.reader(file)
for line in reader:
    t=line[0],line[1]
    print(t)

df = pd.read_csv('Qatif_data.csv')

df.plot(kind='line',x='Date',y='Total Cases',linestyle='-', marker='o',color="Navy", alpha=0.4)
plt.title('Qatif Covid19 Data')
plt.show() 


