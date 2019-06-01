##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas as pd
import numpy as np

df0 = pd.read_csv("tbl0.tsv",sep='\t')
df0['ano'] = [i.split('-')[0] for i in df0['_c3']]
print(df0)

