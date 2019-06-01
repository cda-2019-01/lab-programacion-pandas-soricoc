##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

import pandas as pd
import numpy as np

df0 = pd.read_csv("tbl0.tsv",sep='\t')
x = df0.groupby('_c1')['_c2'].apply(list)
dfx = pd.DataFrame()
dfx['_c0'] = x.keys()
dfx['lista'] = [elem for elem in x]
dfx['lista'] = [":".join(str(v) for v in sorted(elem)) for elem in dfx['lista']]
print(dfx)
