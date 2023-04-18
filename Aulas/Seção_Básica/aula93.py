# Cortando strings.
frase = 'Olha só, que coisa mais interessante!'

lista_palavras = frase.split() # separa (com ' ' por padrão)
lista_frases = frase.split(', ') # separa com o iteravel selecionado

print(lista_palavras)
print(lista_frases)

lista_juntar = ', '.join(lista_frases) # une as frases
print(lista_juntar)