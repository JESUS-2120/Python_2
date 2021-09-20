'''
NAME
        Secuencias_y_Formatos.py

VERSION
        1.0

AUTHOR
         Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>

DESCRIPTION
        Este programa lee un archivo genbank asi como una lista con nombres de genes
        y regresa como output el organismo, la version de la secuencia, fuente del aislado
        y pais de origen anotados en el archivo genbank, de la misma manera busca los
        nombres de genes de la lista en el archivo genbank para retornar como output 15 bases
        del gen asi como la transcripcion y traduccion de dichas 15 bases.

CATEGORY
        Genomic Sequence

Github


INPUT
        Este programa recibe como input un archivo genbank y una lista con nombres de genes

OUTPUT
        Este programa retorna como output el organismo, la version de la secuencia, fuente del aislado
        y pais de origen anotados en el archivo genbank, asi como 15 bases del gen, la transcripcion y
        traduccion de dichas 15 bases correspondientes a cada uno de los genes en la lista.

EXAMPLES
        Input:
                path = "../files/virus.gb"
                Gen = ['G',"M","P"]

        Output:
                Organismo = Isfahan virus
                Version = 1
                Fuente de aislamiento  ['Phlebotomus papatasi']
                Pais ['Iran:Isfahan province']
                Gene = G
                DNA = ATGACTTCAGTCTTA
                RNA = AUGACUUCAGUCUUA
                PROTEINA = MTSVL
                Gene = M
                DNA = ATGAAGAGCTTAAAG
                RNA = AUGAAGAGCUUAAAG
                PROTEINA = MKSLK
                Gene = P
                DNA = ATGTCTCGACTCAAC
                RNA = AUGUCUCGACUCAAC
                PROTEINA = MSRLN
'''

#Importamos las librerias necesarias para trabajar con los formatos
from Bio.Seq import Seq
from Bio import SeqIO

#Definimos la funcion que recibira como argumentos la ruta del archivo y la lista con nombres de genes
def resumen(path,genes):

    #Damos lectura al archivo e imprimimos los datos que nos interesa conocer
    for register in SeqIO.parse(path,"genbank"):
        organismo = register.annotations["organism"]
        version = register.annotations["sequence_version"]

    source = register.features[0]

    print(f"Organismo = {organismo}")
    print(f"Version = {version}")
    print("Fuente de aislamiento ",source.qualifiers["isolation_source"])
    print("Pais",source.qualifiers["country"])

    '''Creamos una estructura con dos for anidados que nos permitira recorrer el 
     archivo genbank en busca de las secuencias de los genes cuyos nombres
     se encuentran en la lista para posteriormente imprimirlas'''
    for j in range(0, len(genes)):
        gen = "['"+genes[j]+"']"
        for i in range(2, len(register.features) , 2):
            if (str(gen) == str(register.features[i].qualifiers["gene"]) ):
                start = register.features[i].location.nofuzzy_start
                end = int(start) + 15
                sec = register.seq[start:end]
                print(f"Gene = {genes[j]}")
                print(f"DNA = {sec}")
                print(f"RNA = {sec.transcribe()}")
                print(f"PROTEINA = {sec.translate()}")
        gen = ""

#Se introduce de manera amable al usuario
print("Bienvenido a Secuencias y Formatos :D\n")
desicion = input("Desea usar el archivo genbank por default? [S/N]: ")

#Se pregunta al usuario si desea ingresar su propio archivo genbank y se guarda el path
if desicion == "S":
    path = "../files/virus.gb"
else:
    path = str(input("Introduzca la ruta de su arcivo genbank: "))

#Se pide al usuario que ingrese los nombres en la lista
print("Intoduzca su lista de nombres de genes")
c = int(input("Ingrese cuantos nombres hay en su lista: "))

i = 0
Gen = []

while i < c:
    i += 1
    print("Ingrese el nombre: ")
    nombre_user = input().upper()
    Gen.append(nombre_user)

resumen(path,Gen)