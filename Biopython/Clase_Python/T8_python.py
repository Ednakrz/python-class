'''
NOMBRE
T8_python
VERSION
  1.0 

AUTOR
 Edna Karen Rivera Zagal <ednakrz@lcg.unam.mx>

 SINOPSIS
    python .\T8_python.py

DESCRIPCION
   Este programa está diseñado pora obtener los codones de las secuencias del archivo Fasta 'seq.nt.fa', y devolver cada uno de estos resultados 
   en un archivo de salida correspondiente a cada marco de lectura dentro de mi archivo.


CATEGORIA
    Bioiformática

OPCIONES 
    Este programa no cuenta con opciones para ingresar datos por el memento, por favor sigue el ejemplo de la forma para ejecutar el programa. 
USO 
Forma en la que se puede ejecutar el programa: 
  ejemplo: python .\T8_python.py

Ejemplo
  Linea de comando usada para el ejemplo: 
  python .\T8_python.py

  El progrma no devuelve algo dentro de la terminal, pero en el repostorio donde está el programa y el archivo origen se encontrarán los archivos de 
  salida. 

  frame_{seq_id}.txt
'''
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


    


