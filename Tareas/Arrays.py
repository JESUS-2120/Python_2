'''
NAME
        Arrays.py
        
VERSION
        1.0
        
AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>
      
DESCRIPTION
        Este programa imprime a pantalla una serie de arrays estructurados
        
CATEGORY
        Arrays
        
INPUT
        Este programa no recibe ningun input
        
EXAMPLES
		
	Output:
		El array estructurado de la produccion de metabolito:

		[('Gen 1',  5., 3.) ('Gen 2', 11., 7.) ('Gen 3',  4., 9.)
		 ('Gen 4',  2., 6.)]
		
		El array estructurado del costo de induccion:

		[('Gen 1', 3.5) ('Gen 2', 5. ) ('Gen 3', 7. ) ('Gen 4', 4.3)]
		
		El array estructurado del costo g/L:

		[('Gen 1', 1.42857143, 0.85714286) ('Gen 2', 2.2       , 1.4       )
		 ('Gen 3', 0.57142857, 1.28571429) ('Gen 4', 0.46511628, 1.39534884)]
        
GITHUB
        https://github.com/JESUS-2120/Python_2/blob/main/Tareas/Arrays.py
'''

#Importmos la libreria necesaria
import numpy as np

#Creamos los arrays estructurados
produccion_metabolito = np.array([('Gen 1',5,3),('Gen 2',11,7),('Gen 3',4,9),('Gen 4',2,6)],dtype = [('Genes',(np.str_,10)),('30 °C',np.float64),('35 °C',np.float64)])

costo_induccion = np.array([('Gen 1',3.5),('Gen 2',5),('Gen 3',7),('Gen 4',4.3)], dtype=[('Genes',(np.str_,10)),('Costo de induccion',np.float64)])

costo_gl = np.array([('Gen 1',1.42857143,0.85714286),('Gen 2',2.2,1.4),('Gen 3',0.57142857,1.28571429),('Gen 4',0.46511628,1.39534884)],dtype=[('Genes',(np.str_,10)),('30 °C costo gl',np.float64),('35 °C costo gl',np.float64)])

#Imprimimos los arrays a pantalla
print("El array estructurado de la produccion de metabolito:\n")
print(produccion_metabolito)
print("\nEl array estructurado del costo de induccion:\n")
print(costo_induccion)
print("\nEl array estructurado del costo g/L:\n")
print(costo_gl)
