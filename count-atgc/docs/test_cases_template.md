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
- Resultado esperado: Los simbolos eesperados no aparecen 0 veces en la cadena
- Estado:
```
El símbolo A aparece 0 veces en la cadena.
El símbolo T aparece 0 veces en la cadena.
El símbolo G aparece 0 veces en la cadena.
El símbolo C aparece 0 veces en la cadena.
```
