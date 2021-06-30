import numpy as np

a = np.array([1,2,3])
print(a)#array

b = np.array([
 (1, 2, 3),
 (4, 5, 6)
]) #matriz
print(b)

c = np.zeros((4, 4)) #Cria de acordo com o número
print(c)

d = np.eye(5, 5) #Cria uma matriz cuja as linhas e as colunas serão iguais ao parametro 
print(d)

#Se usa o numpy para trabalhar com arrays e matrizes