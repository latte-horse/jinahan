import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as pit
import seaborn as sns

df = pd.DataFrame(columns=['x','y'])
df.loc[0]=[3,1]
df.loc[1]=[4,1]
df.loc[2]=[3,2]
df.loc[3]=[4,2]
df.loc[4]=[10,5]
df.loc[5]=[10,6]
df.loc[6]=[11,6]
df.loc[7]=[11,6]
df.loc[8]=[15,2]
df.loc[9]=[15,1]
df.loc[10]=[16,1]
df.loc[11]=[16,2]
df.head(20)
print(df.head(20))

sns.lmplot('x','y',data=df, fit_reg=False, scatter_kws={"s":200})
pit.title('kmean plot')
pit.xlabel('x')
pit.ylabel('y')
