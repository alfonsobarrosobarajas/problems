'''
Aplicación para resolver ecuaciones lineales v1.0.0
@author: P. Barroso
@since: 2022-10-01
'''
import numpy as np


r = int(input('Número de incógnitas: '))
coef_row = []
result_row = []
variable = r + 1


class Simuleq:
    
    def __init__(self):
        pass
    
    def get_data(self):        
        try:
        # Captura de datos
            for i in range(1, r + 1):
                # Número de incógnitas
                print(f'Ecuación {i}: ')
                result = []
                coef = []
                for j in range(1, variable + 1):
                    if opc == 1:
                        x = float(input(f'x{j}: '))
                    else:
                        x = np.random.uniform(-1, 1)
                    if j < variable:
                        coef.append(x)
                    else:
                        result.append(x)
                
                coef_row.append(coef)
                result_row.append(result)
                    
            coeficients = np.array(coef_row)
            results = np.array(result_row)

            # Salida de información
            print(f'Coeficientes\n{coeficients}')
            print(f'Columna de resultados\n{results}')

            x = np.linalg.inv(coeficients).dot(results)

            return x
            # print(f'Solucion del sistema X= \n{x}')
        except Exception as ex:
            raise ex
            # print(ex)