##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas as pd
import numpy as np

df2 = pd.read_csv('tbl2.tsv', sep='\t')
df2['_c5'] = df2['_c5a'] + ":" + df2['_c5b'].astype('str')
x = df2.groupby('_c0')['_c5'].apply(list)
dfx = pd.DataFrame()
dfx['_c0'] = x.keys()
dfx['lista'] = [elem for elem in x]
dfx['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in dfx['lista']]
print(dfx)
