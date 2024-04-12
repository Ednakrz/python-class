# **Contador de ATCG**

Fecha: 02/04/2024

**Participantes / Autor**: Edna Karen Rivera Zagal 

- Edna Rivera <ednakrz@lcg.unam.mx>

## Descripción del Problema
El estar contando de manera manual la aparicion de diferentes nucleotidos como A,T,G y C es un inconveniente cuando hablamos de secuencias muy largas que inclusive pueden llegar a ser de algunas Kb de extensión, ya que al ser tantas se deja mucho espacio para el factor error humano.  

## Especificación de Requisitos

Requisitos funcionales

- Leer diferentes letras (A,T,G,C)de un archivo dado.
- Convierte las letras minusculas a mayusculas. 
- Calcular la aparición de cada tipo de letra leída del archivo.
- Poporionar un archivo de texto plano. 


Requisitos no funcionales
- El script deberá estar escrito en Python.
- El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.


## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en Python, así como el manejo de excepciones para la validación de datos y archivo. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:
 

pseudocogido:

```
#Itroducir el archivo donde se encuentra la cadena
with open('archivo.txt', 'r') as file:

for in archivo.file
 for letra in cadena:
    if letra == 'A':
        count_A += 1
    elif letra == 'T':
        count_T += 1
    elif letra == 'G':
        count_G += 1
    elif letra == 'C':
        count_C += 1
print "La cantidad de veces que apareció A fue:{count_A}"
```
El formato de los datos de entrada será un archivo de tipo txt.

#### Caso de uso:

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-----------------+
         | suma las canti  |
         | dades de veces  |
         | que encuentra   |
	 |una letra,la alma|
	 |cena y la imprime|
         +-----------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo de entrada de texto plano con formato FASTA. El sistema valida el archivo y los datos de entrada, calcula la suma de las letras y muestra el resultado.
- **Flujo principal**:
 	1. El actor inicia el sistema proporcionando el archivo de entrada con las 	letras a sumar.
	2. El sistema valida el archivo y los datos de entrada.
	3. El sistema calcula la suma de apariciones de las letras.
	4. El sistema muestra el resultado.
	
- **Flujos alternativos**:
	- Si los datos de entrada del archivo, en este caso las letras se encuentran en minusculas el progrmas las pasa a 	mayusculas.
