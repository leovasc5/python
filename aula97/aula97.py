import pandas as pd
import numpy as np

p1 = pd.Series([1,2,3,4,5], name="Crescente")
p2 = pd.Series([10,9,8,7,6], name="Decrescente")

a = pd.DataFrame({p1.name:p1, p2.name:p2})
print(a)

for i in a.columns:
    print("Coluna: "+i)