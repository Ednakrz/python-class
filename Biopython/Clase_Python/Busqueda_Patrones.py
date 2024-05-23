
from Bio.Seq import Seq
from Bio import SeqUtils
from Bio import SeqIO 

pattern = Seq("ACG")
sequence1 = ("ATACTATACTAGCTACGACTCGACTACCGACAGACTACGT")

results = SeqUtils.nt_search(str(sequence1),pattern)

print(results)

consensus = "RGWYV"

sequence2 = "CGTAGCTAGCTCAGAGCAGGGACACGTGCTAGCAACAGCGCT"
resultado2= SeqUtils.nt_search(sequence2,consensus) #Imprime donde encontró la secuencias y su posicion 
print (resultado2) 

for seq_record in SeqIO.parse({"seq.nt.fa"},"fasta"):
    print ('Len{}'.format(len(seq_record)))
    print("IID".format(seq_record.id))