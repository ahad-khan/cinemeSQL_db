import pandas as pd
from pandas import ExcelWriter, ExcelFile

CinemaName = []
CinemaManager = []
CinemaAddress = []
CinemaPhone = []

df = pd.read_excel('Cinema.xlsx')
for i in df.index:
    CinemaName.append((df['CinemaName'][i]))
    CinemaManager.append((df['CinemaManager'][i]))
    CinemaAddress.append((df['CinemaAddress'][i]))
    CinemaPhone.append((df['CinemaPhone'][i]))
    print(CinemaName[i])
    print(CinemaManager[i])
    print(CinemaAddress[i])
    print(CinemaPhone[i])