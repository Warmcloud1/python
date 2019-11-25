import pandas as pd
import csv
open_file1='a.csv'
df = pd.read_csv(open_file1)
with open(open_file1,'r',newline='',encoding='utf8') as filex1:
    filereadera=csv.reader(filex1)
    #print(filereadera[0])
    headera=next(filereadera)
titlea=[n for n in headera if n!='']
print(df)
print(titlea)
