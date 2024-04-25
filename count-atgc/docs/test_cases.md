# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrollado para contar la cantidad de apariciones de las letras (A,T,C,G) en un archivo.txt. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para contar las veces que aparecen las letras  'A,T,G,C' en un archivo.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.
    
    
### Caso de prueba 1: Comprobación del conteo correcto de las apariciones de las letras.

- Descripción: Verificar que el script puede contar las veces que aparecen las letras 'A,T,G,C' en el archivo ""archivo.txt
- Datos de entrada: AAAATTTTGGGGCCCC
- Resultado esperado: A=4,T=4,G=4,C=4
- Estado:
```
El símbolo A aparece 4 veces en la cadena.
El símbolo T aparece 4 veces en la cadena.
El símbolo G aparece 4 veces en la cadena.
El símbolo C aparece 4 veces en la cadena.
```

### Caso de prueba 2: Comprobación de error si la cadena de texto no tiene los caracteres esécificados.

- Descripción: Verificar que el script no reconoce otras letras ademas de las ya especificadas.
- Datos de entrada: EEEEFFFFNNNNNOOOO
- Resultado esperado:"Sequence contains invalid character"
Código de entrada:
```
python .\COUNT_ATCG.py .\test.txt
¿Desea ingresar letras específicas? (s/n): n
```
Resultado: 
```
ValueError: Sequence contains invalid character
```

### Caso de prueba 3: Introducir una letra específica.
- Descripción: Verificar que el script reconoce las letras especificadas por el 
 usuario.
- Datos de entrada: A G
- Resultado esperado: Las letras especificadas aparecen 4 veces cada una. 

Código de entrada:
```
python COUNT_ATGC.py .\test.txt
¿Desea ingresar letras específicas? (s/n): S
Ingrese las letras separadas por espacios: A G
```
Resultado: 
```
El símbolo A aparece 4 veces en la cadena.
El símbolo G aparece 4 veces en la cadena.
```
### Caso de prueba 4: Comprobar que el programa no acepta letras no especificadas en el código (A,T,G,C) introducidas por el usuario.
- Descripción: Verificar que el script no reconoce las letras especificadas por el 
 usuario que no sean las declaradas en el código.
- Datos de entrada: E F
- Resultado esperado: "There are invalid character" 

Código de entrada:
```
python COUNT_ATGC.py .\test.txt
¿Desea ingresar letras específicas? (s/n): S
Ingrese las letras separadas por espacios: E F
```
Resultado: 
```
ValueError: There are invalid character
```
### Caso de prueba 5: Comprobar que el programa no lee las letras especificadas en el código (A,T,G,C) introducidas por el usuario, con letras que no están especificadas en el programa.
- Descripción: Verificar que el script no reconoce las letras especificadas por el 
 usuario con letras que no sean las declaradas en el código.
- Datos de entrada: A E G
- Resultado esperado: There are invalid character.  

Código de entrada:
```
python COUNT_ATGC.py .\test.txt
¿Desea ingresar letras específicas? (s/n): S
Ingrese las letras separadas por espacios: A E G
```
Resultado: 
```
ValueError: There are invalid character
```
### Caso de prueba 6: Comprobar que el script acepta los caracteres válidos (ATGC) en minusculas. 
- Descripción: Verificar que el script reconoce las letras especificadas, ya sea que estén en el archivo .txt en minusculas.
- Datos de entrada: atcg
- Resultado esperado: contará los caracteres de la cadena.

Código de entrada: 
```
python .\COUNT_ATCG.py .\test.txt
¿Desea ingresar letras específicas? (s/n): n
```
Resultado: 
```
El símbolo A aparece 1 veces en la cadena.
El símbolo T aparece 1 veces en la cadena.
El símbolo G aparece 1 veces en la cadena.
El símbolo C aparece 1 veces en la cadena.
```

### Caso de prueba 7: Comprobar que el script acepta los caracteres válidos (ATGC) en mayusculas. 
- Descripción: Verificar que el script reconoce las letras especificadas, ya sea que estén en el archivo .txt en mayusculas.
- Datos de entrada: ATGC
- Resultado esperado: contará los caracteres de la cadena.

Código de entrada: 
```
python .\COUNT_ATCG.py .\test.txt
¿Desea ingresar letras específicas? (s/n): n
```
Resultado: 
```
El símbolo A aparece 1 veces en la cadena.
El símbolo T aparece 1 veces en la cadena.
El símbolo G aparece 1 veces en la cadena.
El símbolo C aparece 1 veces en la cadena.
```
### Caso de prueba 8: Comprobar que el script devuelve un mensaje de error en caso de que se introduzca un archivo vacio.
- Descripción: Verificar que el script devuelve un mensaje de error en caso de que se introduzca un archivo vacio.
- Datos de entrada: 
- Resultado esperado: "sorry, the file is empty.".

Código de entrada: 
```
python .\COUNT_ATCG.py .\test.txt
```
Resultado: 
```
ValueError: sorry, the file is empty.
```
### Caso de prueba 9: Comprobar que el script devuelve un mensaje de error en caso de que no se encuentre el archivo.
- Descripción: Verificar que el script devuelve un mensaje de error en caso de que no se encuentre el archivo en la memoria.si es en la memoria ? o es en la terminal? me puedes corregir porfis:).
- Datos de entrada: hola.txt
- Resultado esperado: "Sorry, couldn't find the file.".

Código de entrada: 
```
python .\COUNT_ATCG.py .\hola.txt
```
Resultado: por qué me aparece este mensaje y no el especificado en ingles en mi except?, igual me puedes corregir porfis:). gracias:). 
```
FileNotFoundError: [WinError 2] El sistema no puede encontrar el archivo especificado: 'hola.txt'
```
