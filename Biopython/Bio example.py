import Bio.Seq
from Bio.Seq import MutableSeq #Esto lo teniamos que hacer pero solo se quedó hablado, pero viene en las diapos 
from Bio import SeqUtils

seqobj= Bio.Seq.Seq("ATCGATCGATCGAT")

seq_str = str(seqobj)
print ("{} tiene {} nucleotidos".format(seq_str,len(seq_str)))

# seqobj[0]="T" no se puede porque no puedes modificar los objetos de tipo secuencia 

seq_str = seq_str [::-1] #Con esto volteas la cadena de carcateres 
print (seq_str)

#Falta sacar el complementario pero mee perdí y ya no lo hice, pero viene en las diapos 
#Hay no mejor terminalo luego porque ya quedaste atras unu


