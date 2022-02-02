# 2. crear un programa donde dada una palabra, se busque en una frase y devuelva la cantidad de veces
# que aparece en ella.
def repetidora(palabra, frase):
    contador = frase.count(palabra)
    return contador