'''
NAME
Contador de ATGC    

VERSION
  1.2     

AUTHOR
 Edna Karen Rivera Zagal <ednakrz@lcg.unam.mx>

 SYNOPSIS
    python COUNT_ATGC -inputfile <file> [s] --nucleotidos

DESCRIPTION
   Este progrma suma la cantidad de apariciones de una letra (A,T,G,C) de un archivo .txt.     

CATEGORY
    Contador de frecuencia de nucleótidos en secuencias de ADN.

OPCIONES 
    inputfile 
      Path del archivo que contenga la secuencia de nucelótidos 
        ejemplo: archivo.txt
      Ejecutado el programa te pedirá si quieres buscar una letra específica, para esto seleccionamos: 
      [s] = sí, [n] = no. 
USAGE 
Forma en la que se puede ejecutar el programa: 
  ejemplo: % python archivo.txt

Ejemplo
  Linea de comando usada para el ejemplo: 
  python COUNT_ATCG.py dna_sequence.txt 
  ¿Desea ingresar letras específicas? (s/n): s
  Ingrese las letras separadas por espacios: A G
'''
import sys, os

# Verificar si se proporcionó el nombre del archivo como argumento
if len(sys.argv) < 2:
    print("Uso: python count_atgc.py <nombre_del_archivo>")
    sys.exit(1)

# Obtener el nombre del archivo de los argumentos de la línea de comandos
nombre_archivo = sys.argv[1]

#Verificar que el archivo no este vacio
tamaño_archivo = os.path.getsize(nombre_archivo)
if tamaño_archivo == 0: 
    raise ValueError("sorry, the file is empty.")
   
# Inicializar contadores para cada símbolo
count_A = 0
count_T = 0
count_G = 0
count_C = 0

# Letras específicas proporcionadas por el usuario
specific_letters = []

# Verificar si se especificaron letras específicas
if input("¿Desea ingresar letras específicas? (s/n): ").lower() == 's':
    letters_input = input("Ingrese las letras separadas por espacios: ")
    specific_letters = letters_input.split()
    # Manda error si los caracteres introducidos por el usuario no son validos
    if not all(c in 'ATCG' for c in specific_letters):
            raise ValueError("There are invalid character")

try:
     # Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as file:
        # Leer la cadena del archivo y convertirla a mayúsculas
        cadena = file.read().upper()
        if not all(c in 'ATCG' for c in cadena):
            raise ValueError("Sequence contains invalid character")


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

    # Imprimir el resultado de las letras específicas o de todos los nucleótidos
    if specific_letters:
        for letra in specific_letters:
            if letra == 'A':
                print(f'El símbolo A aparece {count_A} veces en la cadena.')
            elif letra == 'T':
                print(f'El símbolo T aparece {count_T} veces en la cadena.')
            elif letra == 'G':
                print(f'El símbolo G aparece {count_G} veces en la cadena.')
            elif letra == 'C':
                print(f'El símbolo C aparece {count_C} veces en la cadena.')
    else:
        print(f'El símbolo A aparece {count_A} veces en la cadena.')
        print(f'El símbolo T aparece {count_T} veces en la cadena.')
        print(f'El símbolo G aparece {count_G} veces en la cadena.')
        print(f'El símbolo C aparece {count_C} veces en la cadena.')

except FileNotFoundError:
    print(f"Sorry, couldn't find the file'{nombre_archivo}'.")




