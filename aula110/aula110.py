import os
from pathlib import Path
import pandas as pd

p = Path(os.getcwd())

caminho = str(p.parent) + "\\Desktop"
print(caminho)

dados = pd.read_csv(caminho+"\\euro2020.csv")
print(dados.head())

for i in os.sys.path:
    print(i)