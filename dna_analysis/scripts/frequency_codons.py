"""
calculate_at_content.py: Script para calcular la frecuencia de codones en una secuencia de ADN.

Este script lee una secuencia de ADN desde un archivo dado y calcula la frecuencia de codones 
en esa secuencia. La secuencia de ADN debe estar en un archivo de texto y solo
contener los caracteres 'A', 'C', 'G', 'T', o 'N' (este último representa cualquier nucleótido). 
Uso:
    python calculate_at_content.py <path_to_dna_file> [--normalize]

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.
    --normalize        : Opción para normalizar el contenido de AT excluyendo 'N's del c
"""

import argparse
from operations.count_codones import count_codons
from utils.file_io import read_dna_sequence

def main():
    parser = argparse.ArgumentParser(description="Calcula la frecuencia de codones en una secuencia de ADN.")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument("-n", "--normalize", action="store_true", help="Normaliza el contenido de AT excluyendo 'N's del cálculo.")

    args = parser.parse_args()
    file_path = args.file
    normalize = args.normalize

    try:
        # Leer la secuencia del archivo especificado utilizando la función proporcionada por file_io.py
        sequence = read_dna_sequence(file_path)
        
        # Calcular el contenido de AT de la secuencia utilizando la función proporcionada por at_content.py
        frecuencia = count_codons(sequence)
        
        # Mostrar el resultado al usuario
        print(f"La frecuencia de codones en la secuencia es: {frecuencia}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()