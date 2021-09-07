
from Bio.Seq import Seq
from Bio.Seq import  MutableSeq

seqobj = Seq("ATCGCG")
print(str(seqobj))

mutable = MutableSeq(seqobj)
mutable[0] = "n"

print(seqobj.complement())
print(seqobj.reverse_complement())
print(seqobj.translate())
rna = seqobj.transcribe()
print(rna.back_transcribe())
print(seqobj[0:3])

import re

for codon in re.findall(r"(.{3})", str(seqobj)):
    print(codon)

from Bio import SeqUtils
from Bio.SeqUtils import nt_search

patron = Seq("ACG")
sequence = Seq("AATTTTCGGCGTACTGACGCCCTTGAACG")
resultado = nt_search(str(sequence), patron)
print(resultado)


#-------------------------------------------Ejercicio 1------------------------------------------

sequence = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG ")
inicio = Seq("ATG")
posicion = nt_search(str(sequence), inicio)

for i in range(1, len(posicion)):  #Empieza en posicion 1 para saltar patron a buscar
    #Se guarda secuencia en posicion de codon de inicio
    seq_prot = sequence[i:]
    #Traducir secuencia hasta codon de paro
    proteina = seq_prot.translate(to_stop= True)
    print(proteina)
#-----------------------------------------------------------------------------------------------------

from Bio import SeqIO
filename = '../files/seq.nt.fa'
#Revisa cada seqrecords del archivo filename
for seq_record in SeqIO.parse(filename, "fasta"):
    print("ID {}".format(seq_record.id))
    print("len {}".format(len(seq_record)))
    print("Traduccion {}".format(seq_record.seq.translate(to_stop = True)))

#Leer archivo en diccionario
id_dict = SeqIO.to_dict((SeqIO.parse(filename, "fasta")))
print(id_dict["seq4"].seq.transcribe())

id_list = list(SeqIO.parse(filename, "fasta"))
print (id_list[-1].seq)


#Ejercicio 2
filename = "../files/seq.nt.fa"
id_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))
for i in id_dict:
    print(">{}".format(i))
    sec = id_dict[i].seq
    for codon in re.findall(r".{3}", str(sec[1:])):
        print (codon, end = "\t")
    print("\n")

#Leer archivo fastq
n = 0
for record in SeqIO.parse("../files/sample.fastq", "fastq"):
    if n > 2:
        print("%s %s" % (record.id, record.seq))
        n += 1
    else:
        break

print(record.letter_annotations["phred_quality"])

#Ejercicio 3
path = "../files/sample.fastq"

for record in SeqIO.parse(path, "fastq"):
    sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quaity"])
    if (promedio > umbral):
        temp = (promedio, record.id)
        mala_calidad.append(temp)
