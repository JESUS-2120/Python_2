'''
NAME
        ExPASy.py
        
VERSION
        1.0
        
AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>
        Mateo Maya Martinez <mateom@lcg.unam.mx>
        
DESCRIPTION
        Este programa recibe como inputs una serie de IDs y GOs, y retorna como output 
        un archivo .txt con informacion correspondiente a los IDs
        
CATEGORY
        Data Base
        
INPUT
        Este programa unicamente recibe como inputs las listas que contienen los IDs y 
        GOs
        
EXAMPLES
        Input:
        	IDS = ["A0A0K2RVI7_9BETC","A8R4D4_9BETC","POLG_YEFV1",
        	"POLG_DEN1W","Q6W352_CVEN9","D9SV67_CLOC7","A9KSF7_LACP7"
        	,"B8I7R6_RUMCH"]

		GOS = ["GO:0046755","GO:0046761","GO:0046760","GO:0039702",
		"GO:0046765","GO:0046762"]
		
	Output:
		Su archivo esta listo bajo el nombre ExPASy_out.txt :)
		
		> para el ID: {A0A0K2RVI7_9BETC} El abstract es:

		1. Arch Virol. 2015 Nov;160(11):2903-6. doi: 10.1007/s00705-015-2565-1. Epub 2015
		Aug 14.

		Complete genome analysis of equine coronavirus isolated in Japan.

		Nemoto M(1), Oue Y(2), Murakami S(3), Kanno T(4), Bannai H(5), Tsujimura K(5),
		Yamanaka T(5), Kondo T(5).

		Author information: 
		(1)Epizootic Research Center, Equine Research Institute, Japan Racing
		Association, 1400-4 Shiba, Shimotsuke, Tochigi, 329-0412, Japan.
		nemoto_manabu@equinst.go.jp.
		(2)Hokkaido Kushiro Livestock Hygiene Service Center, 127-1 Otanoshike, Kushiro, 
		Hokkaido, 084-0917, Japan.
		(3)Thermo Fisher Scientific, Life technologies Japan Ltd., Sumitomo Fudosan Mita 
		Twin Bldg., 4-2-8 Shibaura, Minato-ku, Tokyo, 108-0023, Japan.
		(4)Dairy Hygiene Research Division, Hokkaido Research Station, National Institute
		of Animal Health, 4 Hitsujigaoka, Toyohira, Sapporo, Hokkaido, 062-0045, Japan.
		(5)Epizootic Research Center, Equine Research Institute, Japan Racing
		Association, 1400-4 Shiba, Shimotsuke, Tochigi, 329-0412, Japan.

		Equine coronavirus has been responsible for several outbreaks of disease in the
		United States and Japan. Only one complete genome sequence (NC99 isolated in the 
		US) had been reported for this pathogenic RNA virus. Here, we report the complete
		genome sequences of three equine coronaviruses isolated in 2009 and 2012 in
		Japan. The genome sequences of Tokachi09, Obihiro12-1 and Obihiro12-2 were
		30,782, 30,916 and 30,916 nucleotides in length, respectively, excluding the
		3'-poly (A) tails. All three isolates were genetically similar to NC99
		(98.2-98.7%), but deletions and insertions were observed in the genes nsp3 of
		ORF1a, NS2 and p4.7.

		DOI: 10.1007/s00705-015-2565-1 
		PMCID: PMC7086706
		PMID: 26271151  [Indexed for MEDLINE]


		> El GO encontrado es:
		GO:0046760
		> Nombre de la proteina:
		Envelope small membrane protein 
		> La definicion del GO es:
		CoV_E
		> El Organismo al que pertence la proteina es:
		Equine coronavirus.
		> La localizacion subcelular es:
		 Host Golgi apparatus membrane 

        
GITHUB
        https://github.com/JESUS-2120/Python_2/blob/main/Tareas/ExPASy.py
'''

#Importamos las librerias necesarias
from Bio import Entrez
from Bio import ExPASy
from Bio import SwissProt
from os import remove
from os import path

#Incluimos email
Entrez.email = "victorec@lcg.unam.mx"


#Definimos la funcion
def expasy(IDS,GOS):
	
	#Eliminamos el archivo en caso de existir
	if path.exists("ExPASy_out.txt"):
		remove("ExPASy_out.txt")
           
        #Definimos el archivo output
	Archivo = "ExPASy_out.txt"


	#Recorremos la lista de IDs
	for i in range(0,len(IDS)):
	
		condicion = 2
		
		#Se declaran el handle y record
		han = ExPASy.get_sprot_raw(IDS[i])
		record = SwissProt.read(han)

		#Buscamos los GO para cada ID
		for j in range(0,len(GOS)):
			
			for k in range(0,len(record.cross_references)):
			
				#En caso de encontrarse un GO recopilamos la informacion
				if (condicion == 2 and GOS[j] == record.cross_references[k][1]):
				
					condicion = 1
					
					#Guardamos el ID del articulo
					ID_articulo = record.references[0].references
					
					#En caso de encontrarse un abstract se imprime, contrario a ello se notifica al usuario
					#Se imprimen tambien los GO e ID
					if len(ID_articulo) > 0:
						
						ID_articulo = ID_articulo[0][1]
					
						with Entrez.efetch(db="pubmed", id=ID_articulo, rettype="abstract", retmode="text") as file:
							with open(Archivo, "a") as handle:
								handle.write("> para el ID: {"+IDS[i]+"} El abstract es:\n"+file.read()+"\n> El GO encontrado es:\n"+GOS[j])
					else:
						with open(Archivo, "a") as handle:
								handle.write("> para el ID: {"+IDS[i]+"}\nNo se encontro un Abstract :c\n> El GO encontrado es:\n"+GOS[j])

		#Se obtienen los nombres, PROSITE ID, localizacion subcelular
		if condicion == 1:
			
			u = 0
			
			nombre = record.description.split("=")[1]
			nombre = nombre.split("{")[0]
			nombre = nombre.split(";")[0]
			
			
			
			with Entrez.efetch(db="pubmed", id=ID_articulo, rettype="abstract", retmode="text") as file:
				with open(Archivo, "a") as handle:
					handle.write("\n> Nombre de la proteina:\n"+nombre+"\n> La definicion del GO es:\n"+record.cross_references[k][2]+"\n> El Organismo al que pertence la proteina es:\n"+record.organism)
					
				for l in range(0, len(record.comments)):
					if "SUBCELLULAR" in record.comments[l]:
						localizacion = record.comments[l].split("SUBCELLULAR LOCATION:")[1]
						localizacion = localizacion.split("{")[0]
						localizacion = localizacion.split(";")[0]
						with open(Archivo, "a") as handle:
							handle.write("\n> La localizacion subcelular es:\n"+localizacion)
							
				for m in record.cross_references: 
					if 'PROSITE' in m:
						with open(Archivo, "a") as handle: 
							handle.write("\n> Prosite ID:" + m[1])
							u += 1
				if u == 0:
					with open(Archivo, "a") as handle: 
							handle.write("\n> No se encontraron PROSITE ID :'(")

			with open(Archivo, "a") as handle:
				handle.write("\n\n---------------------------------------\n\n")	
				
			condicion = 0

		


#Se definen las listas que recibe como input la funcion					
IDS = ["A0A0K2RVI7_9BETC","A8R4D4_9BETC","POLG_YEFV1","POLG_DEN1W","Q6W352_CVEN9","D9SV67_CLOC7","A9KSF7_LACP7","B8I7R6_RUMCH"]

GOS = ["GO:0046755","GO:0046761","GO:0046760","GO:0039702","GO:0046765","GO:0046762"]

#Se llama a la funcion
expasy(IDS,GOS)

#Se indica al usuario el nombre del archivo output
print("Su archivo esta listo bajo el nombre ExPASy_out.txt :)")
