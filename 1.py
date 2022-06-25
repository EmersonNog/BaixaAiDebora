# Importando o metodo choice da biblioteca random.
from random import choice

'''
Criando uma funcao que recebe uma string por parametro e retorna de forma pseudoaleatoria
pelo metodo choice e une todos os item da string com o join. Com o metodo .upper e .lower 
uma string sera setada com seus caracteres maiusculos e minusculos em indices diferentes a cada 
vez que a funcao é chamada.
'''
def StringMaluca(texto):
    print(''.join(choice((str.upper, str.lower))(char) for char in texto))

# Chamando a funcao StringMaluca.
StringMaluca('Linguagem de programacao')
StringMaluca('Linguagem de programacao')
StringMaluca('Linguagem de programacao')
