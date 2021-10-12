'''
NAME
        Tarea_5.py
        
VERSION
        1.0
        
AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>
        
DESCRIPTION
        Empleando Entrez.efetch y Entrez.elink el programa crea un archivo que 
        contenga el abstract y los IDs de articulos que citan articulos obtenidos
        mediante la busqueda en la base de datos pubmed
        
CATEGORY
        Data Base
        
INPUT
        Este programa unicamente recibe como input el string necesario para realizar 
        la  busqueda en pubmed
        
EXAMPLES
        Input:
        	ludosky ma[AUTH] AND (electrocyte[Title] OR Baumannii[Title])
	
	Output:
		Su archivo esta listo en la carpeta files bajo el nombre Abstracts.txt
        
GITHUB
        
'''

#Importamos las librerias necesarias
from Bio import Entrez 
from pprint import pprint 
from os import remove
from os import path

#Ingresamos un correo electronico
Entrez.email = "victorec@lcg.unam.mx"
	
#TAREA 5


print("Bienvenido al buscador automatico\nej. ludosky ma[AUTH] AND (electrocyte[Title] OR Baumannii[Title])\nIngrese un string de busqueda considerando el ejemplo: ")
termino = input()
	
#Buscamos en la base de datos
handle = Entrez.esearch(db="pubmed", term= termino)
record = Entrez.read(handle)

#Creamos el archivo IDs
IDS = open("PycharmProjects/Python_2/files/IDs.txt","w")
IDS.write("Los IDs correspondientes a los articulos de su busqueda son:\n")

#Escribimos los IDs en el archivo que creamos
for rec in record["IdList"]:
	IDS.write("> "+rec+"\n")

IDS.close()

#Creamos el archivo IDs y damos lectura al contenido
archivo_ids = open("PycharmProjects/Python_2/files/IDs.txt")

all_lines = archivo_ids.readlines()

#Creamos la lista vacia ids
ids = []

#del archivo anterior conservammos unicamente los ids
for i in range(1,len(all_lines)):

	Id = all_lines[i].split(" ")
	ids.append(Id[1].replace("\n",""))

#Creamos el archivo Abstracts.txt
if path.exists("PycharmProjects/Python_2/files/Abstracts.txt"):
	remove("PycharmProjects/Python_2/files/Abstracts.txt")

Abstracts = "PycharmProjects/Python_2/files/Abstracts.txt"

#Obtenemos tanto el abstract como los ids de los articulos que citan al articulo para cada id de la lista
for i in range(0,len(ids)):
	
	record = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc", LinkName="pubmed_pmc_refs", from_uid=ids[i]))
	
	id_citas = [link["Id"] for link in record[0]["LinkSetDb"][0]["Link"]]
	
	citas = ""
	
	for j in range(0,len(id_citas)):
		citas = citas + id_citas[j] + ";"
	
	with Entrez.efetch(db="pubmed", id=ids[i], rettype="abstract", retmode="text") as file:
		with open(Abstracts, "a") as handle:
			handle.write("para el ID: {"+ids[i]+"} El abstract es:\n"+file.read()+"los IDs de los articulos que lo citan son:\n"+citas+"\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n")
	

print("Su archivo esta listo en la carpeta files bajo el nombre Abstracts.txt")
