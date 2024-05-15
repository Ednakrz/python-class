"""
count_codones.py: Módulo para calcular la frecuencia de codones en secuencias de ADN.

Este módulo proporciona funciones para determinar la frecuencia de los codones en una secuencia de ADN dada. Esto es útil para estudios genéticos donde
las proporciones de AT pueden ser indicativas de ciertas características genómicas.

Funciones:
- count_codons(dna_sequence): Devuelve la frecuencia de codones en la secuencia.
"""


def count_codons(dna_sequence):
    """
    Calcula la frecuencia de los codones en una secuencia de ADN.

    Args:
        dna_sequence (str): La secuencia de ADN a analizar.
        normalize (bool): Si True, normaliza el contenido de AT en caso de que haya 'N's en la secuencia.

    Returns:
        float: El porcentaje de contenido de AT en la secuencia.

    Raises:
        ValueError: Si la secuencia está vacía o contiene caracteres no válidos.
    """
    codon_freq = {}
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        if len(codon) == 3:
            if codon in codon_freq:
                codon_freq[codon] += 1
            else:
                codon_freq[codon] = 1
    return codon_freq

if __name__ == "__main__":
    # Prueba de funcionalidad.
    dna_sequence_prueba = "ATGCGAATTCGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"

    frecuencia_de_codones = count_codons(dna_sequence_prueba)
    print (frecuencia_de_codones)