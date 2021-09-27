'''
NAME
       Archivos_PDB.py

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

DESCRIPTION
        Dada una ruta a un archivo .pdb, el nombre de una cadena y el
        codigo de tres letras de un aminoacido el programa retorna una lista con
        todos los residuos de esa cadena

CATEGORY
        Proteomic sequence

INPUT
        El input de este programa esta comprendido por la ruta de un archivo pdb, asi como el nombre de una cadena
        y el codigo de tres letras de un aminoacido

OUTPUT
        El programa retorna a pantalla una lista con todos los aminoacidos de interes, o en su defecto un mensaje
        indicando al usuario que no se encontraron los aminacido seleccionados en la cadena

EXAMPLES
        Input:
            Bienvenido al programa Ingrese los datos que se piden para poder buscar los residuos
            Ingrese el nombre de una cadena: a
            Ingrese el nombre de un aminoacido: phe

        Output:
            [<Residue PHE het=  resseq=6 icode= >, <Residue PHE het=  resseq=8 icode= >,
            <Residue PHE het=  resseq=11 icode= >,......]

Github:

'''

#Importamos la libreria Bio
from Bio import PDB

#Creamos un objeto PDBparser
parser = PDB.PDBParser(QUIET = True)

#Definimos la funcion obtener_residuos y pasamos los parametros
def obtener_residuos(path,cadena,residuo):

    #Obtenemos la estructura para poder acceder a los modelos y asi a las cadenas
    estructura = parser.get_structure("Prot_1",path)
    modelo = estructura[0]
    chain = modelo[cadena]

    #Creamos una lista para almacenar los datos que se retornaran al usuario
    lista = []

    #Iteramos sobre la cadena de modo que se guarden en la lista aquellos residuos solicitados por el usuario
    for residuos in chain:
        if residuos.get_resname() == residuo:
            lista.append(residuos)

    #Verificamos si la lista esta vacia y de ser asi se notifica al usuario, caso contrario se retorna la lista
    if len(lista) < 1:
        return("No hay residuos del aminoacido seleccionado en la cadena indicada")
    else:
        return(lista)

print("Bienvenido al programa Ingrese los datos que se piden para poder buscar los residuos")
cadena = input("Ingrese el nombre de una cadena: ")
residuo = input("Ingrese el nombre de un aminoacido: ")
cadena = cadena.upper()
residuo = residuo.upper()
path = input("Ingrese la ruta de un archivo pdb (Si desea utilizar el default oprima enter): ")
if path == "":
    path = "../files/1fat.pdb"
print(obtener_residuos(path,cadena,residuo))
