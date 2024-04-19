# **Contador de ATCG**

Fecha: 19/04/2024

**Participantes / Autor**: Edna Karen Rivera Zagal 

- Edna Rivera <ednakrz@lcg.unam.mx>

## Descripción del Problema
El estar contando de manera manual la aparicion de diferentes nucleotidos como A,T,G y C es un inconveniente cuando hablamos de secuencias muy largas que inclusive pueden llegar a ser de algunas Kb de extensión, ya que al ser tantas se deja mucho espacio para el factor error humano.  

## Especificación de Requisitos

Requisitos funcionales

- Leer diferentes letras (A,T,G,C)de un archivo dado.
- Convierte las letras minusculas a mayusculas. 
- Calcular la aparición de cada tipo de letra leída del archivo.
- Calcular la aparición de un tipo de letra (A,T,G,C) especificado por el usuario.
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

if input("¿Desea ingresar letras específicas? (s/n): ").lower() == 's':

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

except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'.")

except Exception as e:
    print("Error inesperado:", e)
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
         | suma la canti  |
         | dade de veces  |
         | que encuentra   |
	 |una letra,la alma|
	 |cena y la imprime|
         +-----------------+
```

- **Actor**: Usuario

- **Descripción**: El actor proporciona un archivo de entrada de texto plano con formato FASTA. En el primer caso el sistema valida el archivo y los datos de entrada, calcula la suma de las letras y muestra el resultado.

- Para el segundo argumento [s] el programa pregunta si queremos especificar que letra contar, si introducimos el argumento [s], el programa valida los datos y cuenta la apricion de la letra deseada, si el argumento introducido es [n o enter] el archivo cuenta las letras indicadas en el programa por defult.
- 
- **Flujo principal**:
 	- 1.1 El actor inicia el sistema proporcionando el archivo de entrada con 	las 	letras a sumar.
	- 1.2 El sistema valida el archivo y los datos de entrada.
  	- 1.3 El sistema calcula la suma de apariciones de las letras.
  	- 1.4 El sistema muestra el resultado.

  	- 2.1El actor inicia el sistema proporcionando el archivo de entrada con 		las 	letras a sumar.
  	- 2.2 El sistema pregunta si queremos contar una letra en específico.
  	- 2.3 si el argumento ingresado es [s], el programa solo cuenta la 		aparicion 	de la letra introducida por el usuario.
	- 2.4 Si el argumento ingresado es [n o enter ], el programa por defult 		cuenta las apariciones de todas las letras (A,T,G,C).
   	- 2.4 El programa muestra el resultado.
- **Flujos alternativos**:
	- Si los datos de entrada del archivo, en este caso las letras se encuentran en minusculas el programa las pasa a 	mayusculas.

- **Validaciones del programa**:
  	- Si el archivo está vacio se manda un mensaje de error de que el archivo está vacio y por lo tanto no se puede procesar.
  	- Si no se encontró el archivo proporcionado por el usuario el programa mando un mensaje de error de que el archivo no fue encontrado.
  	- Al programa solo acepta cadenas que contengas las letras, A,T,G,C ya sea que esten en mayusculas o minusculas, de no encontrarse el programa mando un mensaje de error en el que se afirma que la secuencia contiene caracteres invalidos.
  	- El programa solo acepta como argumentos las letras 'A','T','G','C', en caso de introducir caracteres diferentes, el programa devuelve un mensaje de error aclarando que los caracteres son invalidos. 
