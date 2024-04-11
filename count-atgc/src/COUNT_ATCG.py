'''
NAME
Contador de ATGC    

VERSION
  1.0      

AUTHOR
 Edna Karen Rivera Zagal <ednakrz@lcg.unam.mx>

 SYNOPSIS
    python3 count_atgc -inputfile <file> 

DESCRIPTION
   Este progrma suma la cantidad de apariciones de una letra (A,T,G,C) de un archivo .txt.     

CATEGORY
    Contador.

OPCIONES 
    inputfile 
      Path del archivo que contenga la secuencia de nucelótidos 
        ejemplo: archivo.txt
USAGE 
Forma en la que se puede ejecutar el programa: 
  ejemplo: % python archivo.txt

Ejemplo
  Linea de comando usada para el ejemplo: 
  python COUNT_ATCG.py dna_sequence.txt
'''

# Inicializar contadores para cada símbolo
count_A = 0
count_T = 0
count_G = 0
count_C = 0

# Abrir el archivo en modo lectura
with open('archivo.txt', 'r') as file:
    # Leer la cadena del archivo y convertirla a mayúsculas
    cadena = file.read().upper()

# Contar las ocurrencias de cada símbolo en la cadena
for letra in cadena:
    if letra == 'A':
        count_A += 1
    elif letra == 'T':
        count_T += 1
    elif letra == 'G':
        count_G += 1
    elif letra == 'C':
        count_C += 1

# Imprimir el resultado
print(f'El símbolo A aparece p veces en la cadena.')
print(f'El símbolo T aparece {count_T} veces en la cadena.')
print(f'El símbolo G aparece {count_G} veces en la cadena.')
print(f'El símbolo C aparece {count_C} veces en la cadena.')




