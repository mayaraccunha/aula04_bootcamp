# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro_01: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "Estagiario",
    "Ano": 2005
}

livro_02: Dict[str, Any] = {
    "Titulo": "Game of Thrones 2",
    "Autor": "Estagiario",
    "Ano": 2007
}

lista_de_elementos = livro_01.items()
for elemento in lista_de_elementos:
    print(elemento)

lista_de_livros = []

lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

print(lista_de_livros)