# Identificar un palindromo 

def palindromo(text):
    text = text.replace(" ", "")
    text = text.lower()
    
    if str(text) == "".join(reversed(text)):
        print("Es palindromo")
    else:
        print("No es palindromo")
        
palindromo("Anita lava la tina")
palindromo("palindromo")

