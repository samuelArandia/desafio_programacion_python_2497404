# Encontrar la primera letra que se repite en un texto

def primera_letra_repetida(text):
    text_sin_espacios = text.replace(" ", "")
    text_minusculas = text.lower()
    
    lista_letras =[]
    for letra in text_minusculas:
        if letra in lista_letras:
            return print("La primera letra que se repite es: ", letra)
        else:
            lista_letras.append(letra)
    
    
    return None
    
primera_letra_repetida("hola mundo")
