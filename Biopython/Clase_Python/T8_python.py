import re
from Bio import SeqIO
from Bio.Seq import Seq
 
for record in SeqIO.parse("seq.nt.fa", "fasta"):
    seq = record.seq
    print ("ID:",record.id)
    codon = re.findall(r"(.{3})", str(seq))
    codon_str = ' '.join(codon)
    print("Codones:",codon_str) 
    print("Secuencia:", record.seq)
    print("Longitud de la secuencia:\n", len(record.seq))


    


