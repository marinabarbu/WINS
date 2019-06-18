import pandas as pd

#f = pd.read_excel(r'C:\Users\Tehnic\PycharmProjects\WINS\SVR\SCP3_raw_25oct_10feb.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
#rint (df)

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('SCP3_raw_25oct_10feb.xlsx', sheetname='SCP3_raw_25oct_10feb')

print("Column headings:")
print(df.columns)
