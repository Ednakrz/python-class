def get_at_content(dna,num): 
    dna = dna.replace ('N','')
    length = len(dna) 
    a_count = dna.upper().count('A') 
    t_count = dna.upper().count('T') 
    at_content = (a_count + t_count) / length 
    return round (at_content,num)


at_content = get_at_content("ATGACTGGACCA",2) # Paso de argumentos por posición 
print("ATGACTGGACCA" + ": " + str(at_content))
print("AT content ATGACTGGACCA  is " + str(get_at_content("ATGACTGGACCA",3)))
print(get_at_content("ATGCGCGATCGATCGAATCG",1))
print (get_at_content ("atctggggatatatagcgcgcatatcgcat",num = 2)) #mezclamos argumentos por posición y por nobre 
print (get_at_content(dna="TACGATC",num=3)) #argumetnos por palabras clave 
# print (get_at_content(dna= "gatagatctcgatcgatcgat",2)) # si lo voy a mezclar siempre tengo que meter primero argumentos posicionales que por nobre 
# por eso debemos de escoger una forma de pasar los argumentos 

#probando la funcion get_at_content

assert get_at_content("ATGC",2) == 0.50 #assert me permite evaluar un resultado esperado, si mi resultado esperado es correcto la funcion si jala bien 
# Si esta correcto no me regresa nada pero si esta mal me dice que hay un error 
# assert get_at_content ("ATCG",2)==0.4 #ESTO ES FALSO Y ME VA A MARCAR UN ERROR 
assert get_at_content ("ATCGNNNNNNNNN",2)==0.5 # CON ESA NOO JALA PORQUE SI ESTA TOMANDO EN CUENTA LAS N Y EL RESULTADO CORRECTO ES OTRO 
#AHORA SI YA JALA PORQUE LE AGREGAMOS LA FUNCION REPLACE QUE CMABIA UN CARACTER POR OTRO, EN ESTE CASO LAS N POR NULOS?
print (get_at_content ("ATCGNNNNNNNNN",2))