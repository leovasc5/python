import pandas as pd
import numpy as np
import os
from pathlib import Path

posicao = np.arange(1,21, 1)
times = ["São Paulo", "Santos", "Internacional", "Grêmio", "Corinthians", "Palmeiras", "Atlético Mineiro", "Flamengo", "Cruzeiro", "Fluminense", 
"Vasco da Gama", "Botafogo", "Athletico Paranaense", "Goiás", "Coritiba", "Bahia", "Sport", "Vitória", "Portuguesa", "Guarani"]
pontos = [2224, 2153, 2143, 2115, 2109, 2102, 2100, 2097, 2086, 1882, 1807, 1702, 1574, 1344, 1279, 1267, 1129, 1107, 896, 889]
jogos = [1511, 1527, 1492, 1522, 1494, 1438, 1507, 1517, 1481, 1446, 1409, 1386, 1187, 1093, 1069, 1103, 982, 972, 781, 709]
vitorias = [667, 650, 650, 646, 636, 653, 640, 635, 636, 558,531, 498, 451, 381, 376, 368, 327, 319, 258, 269]
empates = [442, 429, 418, 424, 439, 397, 415, 426, 403, 403, 427, 400, 311, 301, 291, 343, 269, 259, 249, 215]
derrotas = [402, 448, 424, 452, 419, 388, 452, 456, 442, 485, 451, 488, 425, 411, 402, 392, 386, 394, 274, 225]
gols_pro = [2236, 2263, 2018, 2031, 1962, 2119, 2179, 2094, 2131, 1913, 1926, 1743, 1555, 1401, 1249, 1244, 1113, 1165, 948, 898]
gols_contra = [1598, 1718, 1531, 1602, 1547, 1549, 1769, 1724, 1678, 1734, 1712, 1704, 1453, 1417, 1280, 1333, 1224, 1360, 955, 797]
saldo = [638, 545, 487, 429, 415, 570, 410, 370, 453, 179, 214, 39, 102, -16, -31, -87, -111, -195, -7, 101]

colunas = ["times", "pontos", "jogos", "vitorias", "empates", "derrotas", "gols_pro", "gols_contra", "saldo_de_gols"]

pontuacao_historica = zip(times, pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra, saldo)

df = pd.DataFrame(pontuacao_historica, index=posicao, columns=colunas)
print(df.head(20))

caminho = Path(os.getcwd())
caminho_csv = str(caminho) + "\\aula111\\pontuacao_historica_brasileirao.csv"
caminho_xlsx = str(caminho) + "\\aula111\\pontuacao_historica_brasileirao.xlsx"

df.to_csv(caminho_csv)
df.to_excel(caminho_xlsx)