def palindromo(palabra):
    """
    Función muy sencilla que devuelve si una palabra es o no un palídromo.
    """
    es_palindromo = True # Se define la variable es palindrome como True
    
    for i in range(int(len(palabra)/2)): # vamos caracter a caracter hasta llegar a la mitad de la palabra
        
        if palabra[i] != palabra[-(i + 1)]: # si cuando contamos por una lado un caracter no coincide con el numericamente equivalente del otro lado...
        	es_palindromo = False # ... la palabra no es un palindromo
        	break
    
    return es_palindromo

# print('Predicción:', palindromo('atpa'),'\tRealidad: False') # no palíndromo, par
# print('Predicción:', palindromo('atta'),'\tRealidad: True')  # palíndromo, par
# print('Predicción:', palindromo('atpca'),'\tRealidad: False') # no palíndromo, impar
# print('Predicción:', palindromo('atpta'),'\tRealidad: True') # palíndromo, impar

