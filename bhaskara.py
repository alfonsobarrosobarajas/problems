'''
Ejemplo de uso de la fŕomula de bashkara 'Fórmula General'
'''
import numpy as np


data = []
a = float(input('a: '))
b = float(input('b: '))
c = float(input('b: '))
data.append(a)
data.append(b)
data.append(c)

x1, x2 = np.roots(data)

print(f'x1: {x1};x2: {x2}') 