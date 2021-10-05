'''
NAME
        Tarea_4.py
        
VERSION
        1.0
        
AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>
        
DESCRIPTION
        Empleando Entrez.einfo y ENtrez.read el programa imprime la descripcion 
        de los campos FieldList y LinkList en la base de datos protein, de la misma
        manera dadas palabras claves de busqueda se obtienen los IDs de los articulos
        que coinciden con los criterios de busqueda en la base de datos pubmed
        
CATEGORY
        Data Base
        
INPUT
        Este programa unicamente recibe como inputs las palabras clave para la 
        busqueda de los articulos en la base de datos pubmed
        
EXAMPLES
        Input:
        	Ingrese el termino con el que desea realizar su busqueda: ludosky ma
		Ingrese el campo del termino ingresado: AUTH
		Ingrese el termino con el que desea realizar su busqueda: electrocyte
		Ingrese el campo del termino ingresado: Title
		Ingrese el termino con el que desea realizar su busqueda: Baumannii
		Ingrese el campo del termino ingresado: Title
	
	Output:
		ECNO -> Description:
		EC number for enzyme or CAS registry number


		protein_protein_small_genome -> Description:
		All proteins from this genome

		El archivo con los IDs de su busqueda se encuentra en: ../files/ bajo el nombre IDs.txt
        
GITHUB
        https://github.com/JESUS-2120/Python_2/blob/main/Tareas/Tarea_4.py
'''

#Importamos las librerias necesarias
from Bio import Entrez 
from pprint import pprint 

#Ingresamos un correo electronico
Entrez.email = "victorec@lcg.unam.mx"

#TAREA 1

#Indicamos la base de datos de interes
handle = Entrez.einfo(db = "protein")
record = Entrez.read(handle)

#Obtenemos la descripcion para cada uno de los campos solicitados 
for i in range(0,len(record["DbInfo"]["FieldList"])):
	if record["DbInfo"]["FieldList"][i]["Name"] == "ECNO":
		print(record["DbInfo"]["FieldList"][i]["Name"],"->","Description:")
		print(record["DbInfo"]["FieldList"][i]["Description"])
		print("\n")	


for i in range(0,len(record["DbInfo"]["LinkList"])):
	if record["DbInfo"]["LinkList"][i]["Name"] == "protein_protein_small_genome":
		print(record["DbInfo"]["LinkList"][i]["Name"],"->","Description:")
		print(record["DbInfo"]["LinkList"][i]["Description"])
		print("\n")
		
#TAREA 2


print("Bienvenido al buscador automatico\nSi desea usar el formato ya existente ingrese (1) si desea ingresar su propio string ingrese (2): ")

opc = int(input())

if (opc < 1 or opc > 2):
	
	opc = int(input("Ingrese un numero valido: "))
	
if opc == 1:

	print("Considerando como ejemplo\ntermino = 'ludosky ma[AUTH] AND (electrocyte[Title] OR Baumannii[Title])\ningrese los campos con los que desea realizar su busqueda")

	#Creamos la lista palabras que utilizaremos para guardar las palabras de busqueda
	palabras = ["","","","","",""]

	#Pedimos al usuario las palabras de busqueda
	for i in range(3):
		palabras[i] = str(input("Ingrese el termino con el que desea realizar su busqueda: "))
		palabras[i + 3] = str(input("Ingrese el campo del termino ingresado: "))

	#Concatenamos todo en un string que nos permita concretar la busqueda 
	termino = palabras[0] + "[" + palabras[3] + "]" + " AND (" + palabras[1] + "[" + palabras[4] + "] OR " + palabras[2] + "[" + palabras[5] + "])"

if opc == 2:

	termino = input("Ingrese su string de busqueda: ")
	
#Buscamos en la base de datos
handle = Entrez.esearch(db="pubmed", term= termino)
record = Entrez.read(handle)

#Creamos el archivo IDs
IDS = open("../files/IDs.txt","w")
IDS.write("Los IDs de su busqueda son: \n")

#Escribimos los IDs en el archivo que creamos
for rec in record["IdList"]:
	IDS.write(">" + rec + "\n")
	
print("El archivo con los IDs de su busqueda se encuentra en: ../files/ bajo el nombre IDs.txt")
