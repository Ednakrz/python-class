# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrollado para contar la cantidad de apariciones de las letras (A,T,C,G) en un archivo.txt. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para contar las veces que aparecen las letras  'A,T,G,C' en un archivo.

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.
    
    
### Caso de prueba 1: Comprobación del coneto correcto de las apariciones de las letras.

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

### Caso de prueba 2: Comprobación de error sin una letra.

- Descripción: Verificar que el script no reconoce otras letras ademas de las ya especificadas.
- Datos de entrada: EEEEFFFFNNNNNOOOO
- Resultado esperado: Los simbolos esperados aparecen 0 veces en la cadena
- Estado:
```
El símbolo A aparece 0 veces en la cadena.
El símbolo T aparece 0 veces en la cadena.
El símbolo G aparece 0 veces en la cadena.
El símbolo C aparece 0 veces en la cadena.
```
### Caso de prueba 3: Introducir una letra específica.
- Descripción: Verificar que el script reconoce las letras especificadas por el 
 usuario.
- Datos de entrada: A G
- Resultado esperado: Las letras especificadas aparecen 4 veces cada una. 

Código de entrada:
```
python COUNT_ATGC.py .\PRUEBA.txt
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
- Resultado esperado: El programa no regresa ningun resultado. 

Código de entrada:
```
python COUNT_ATGC.py .\PRUEBA.txt
¿Desea ingresar letras específicas? (s/n): S
Ingrese las letras separadas por espacios: E F
```
Resultado: 
```
```
### Caso de prueba 4: Comprobar que el programa lee las letras especificadas en el código (A,T,G,C) introducidas por el usuario, aun con letras que no están especificadas en el programa.
- Descripción: Verificar que el script  reconoce las letras especificadas por el 
 usuario aun con letras que no sean las declaradas en el código.
- Datos de entrada: A E G
- Resultado esperado: Las letras especificadas aparecen 4 veces cada una.  

Código de entrada:
```
python COUNT_ATGC.py .\PRUEBA.txt
¿Desea ingresar letras específicas? (s/n): S
Ingrese las letras separadas por espacios: A E G
```
Resultado: 
```
El símbolo A aparece 4 veces en la cadena.
El símbolo G aparece 4 veces en la cadena.
```
