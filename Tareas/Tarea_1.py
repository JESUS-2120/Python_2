'''
NAME
       Tarea 1

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>
'''

#Creamos la clase condiciones optimas
class Condiciones_Optimas():

    #Definimos loa atributos
    longitud_dna  = ""
    tipo_dna = "ADN-B"

    #Definimmos el constructor
    def __init__(self, dna_seq):
        self.dna_seq = dna_seq

    #Definimmos los metodos de la clase
    def Estado_Celular(self):
            print("Celula viva :D")

    def RNA_a_PROT(self):
        # Definimos un diccionario con el codigo genetico
        gencode = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
            'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
            'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
            'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
            'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
            'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
            'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
            'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
            'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
            'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
            'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

        # Solicitamos al usuario una secuencia de RNA
        dna = self.dna_seq

        # Se convierten los caracteres a mayusculas y se reemplazan 'U' por 'T'
        dna = dna.upper()
        dna = dna.replace("U", "T")

        # Definimos la variable proteina como una cadena vacia
        proteina = ""

        # Creamos un loop que recorra la secuencia de RNA
        for i in range(0, len(dna), 3):

            # Definimos subcadenas de 3 nucleotidos correpondientes a los codones
            triplete = dna[i: i + 3]

            # Si se llega a un codon de paro se termina la traduccion y se imprime la proteina
            if gencode[triplete] == "_":
                print(proteina)
                exit()

            # Se concatena a la secuencia de la proteina el siguiente aminoacido
            proteina += gencode[triplete]

            print(proteina)

    def Busqueda_codon_inicial(self):
        DNA = self.dna_seq.upper()

        posicion_inicio = DNA.find('TAC')
        posicion_final = DNA.find('ATT')
        if (posicion_final < 0):
            posicion_final = DNA.find('ATC')
        if (posicion_final < 0):
            posicion_final = DNA.find('ACT')
        posicion_final += 3

        ORF = DNA[posicion_inicio:posicion_final]
        mRNA = ORF.replace('T', 'U')

        if (posicion_inicio == 0):
            print('No hay una secuencia codificante en la secuencia introducida')
            print('No existe un codon de inicio para hacer un RNA')
        else:
            print('El codon de inicio comienza en la posicion: ', posicion_inicio + 1, ' y termina en la posicion: ',
                  posicion_final)
            print('La secuencia del mRNA es: \n' + mRNA)

#Creamos la clase condiciones salinas que hereda a la clase anterior
class Condiciones_Salinas(Condiciones_Optimas):

    # Definimos loa atributos
    tipo_dna = "ADN-A"
    respuesta_apoptotica = "SI"

    #Creamos un polimorfismo de la funcion estado celular
    def Estado_Celular(self):
        print("Celula muerta :c")

Coli = Condiciones_Salinas("")
Coli.Estado_Celular()