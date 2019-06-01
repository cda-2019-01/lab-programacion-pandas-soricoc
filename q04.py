##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np

df1 = pd.read_csv("tbl1.tsv",sep='\t')
dif = df1['_c4'].unique()
s = []
for d in dif:
    s.append(d.upper())
s = sorted(s)
print(s)
