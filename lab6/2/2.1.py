#2.1
import pandas as pd
import numpy as np


indexes = list(range(1,7))
columns = ['A','B','C','D']
data = np.random.randint(10,size=(6,4))

df = pd.DataFrame(data=data,index=indexes,columns=columns,dtype=np.float32)
print('************** df **************')
print(df)

#2.2
print('************** head **************')
print(df.head(2))

print('************** tail **************')
print(df.tail(2))

#2.3
print('************** values= make a numpy **************')
print(df.values)

print('************** columns= label of columns **************')
print(df.columns)

print('************** index= label of index **************')
print(df.index)

print('************** describe= statistic calculations **************')
print(df.describe())

#2.4
df.sort_values(by=['B','C'],ascending=[False,True],inplace=True)
print('************** sort **************')
print(df)

#2.5
data1 = np.random.randint(10,size=6)
S = pd.Series(data=data1 ,name='F',index=indexes,dtype=np.float32)
df = df.merge(S.to_frame(), left_index=True,right_index=True)
print('************** merge **************')
print(df)

#2.6
df = df.sort_index()
df.at[3,'F'] = np.nan
df.at[5,'F'] = np.nan
print('********************** np.nan **************')
print(df.loc[1:3,['A','F']])

#2.7
df1 = df.dropna()
print('************** dropnan **************')
print(df1)


#2.8
df1 = df.fillna(np.mean(df['F']))
print('************** fillnan **************')
print(df1)