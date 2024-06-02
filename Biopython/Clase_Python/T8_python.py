






import re
from Bio import SeqIO
from Bio.Seq import Seq
 

for record in SeqIO.parse("seq.nt.fa", "fasta"):
    seq_id = record.id
    output_filename = f"frame_{seq_id}.txt"
    with open(output_filename, "w") as output_file: 
        output_file.write("ID: " + record.id + "\n")
        seq = record.seq
        codon = re.findall(r"(.{3})", str(seq))
        codon_str = ' '.join(codon)
        output_file.write("Codones: " + codon_str + "\n")
        output_file.write("Secuencia: " + str(record.seq) + "\n")
        output_file.write("Longitud de la secuencia: " + str(len(record.seq)) + "\n")


    


