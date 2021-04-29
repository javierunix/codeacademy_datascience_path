"""
	Muy sencilla función que determina si una
	palabra es o no un palindromo
	"""

def palindromo(palabra):

    es_palindromo = True # Se define la variable es palindrome como True
    
    for i in range(int(len(palabra)/2)): # vamos caracter a caracter hasta llegar a la mitad de la palabra
        
        if palabra[i] != palabra[-(i + 1)]: # si cuando contamos por una lado un caracter no coincide con el numericamente equivalente del otro lado...
        	es_palindromo = False # ... la palabra no es un palindromo
        	break
    
    return es_palindromo

print('Predicción:', palindromo('atpa'),'Realidad: False') # no palíndromo, par
print('Predicción:', palindromo('atta'),'Realidad: True')  # palíndromo, par
print('Predicción:', palindromo('atpca'),'Realidad: False') # no palíndromo, impar
print('Predicción:', palindromo('atpta'),'Realidad: True') # palíndromo, impar

