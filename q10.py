##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd
import numpy as np

df1 = pd.read_csv("tbl1.tsv",sep='\t')
x = df1.groupby('_c0')['_c4'].apply(list)

dfx = pd.DataFrame()
dfx['_c0'] = x.keys()
dfx['lista'] = [elem for elem in x]
dfx['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in dfx['lista']]
print(dfx)

