import pandas as pd
import numpy as np

data = np.array([['','Col1','Col2','Col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])


df = pd.DataFrame(data,columns=['Col1', 'Col2', 'Col3'])


#Make slices of data:

#   second column using column name
print((df['Col2']))
#  third column using column index (.iloc[])
print((df.iloc[:,2]))
#  slice element at third row of second column (use .iloc())
print(df.iloc[2][1])
