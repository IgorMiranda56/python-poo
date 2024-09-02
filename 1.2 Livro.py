import os

os.system("clear || cls") # Limpar terminal.

class Livro:
    # Construtor.
    def __init__(self, titulo: str, autor: str, numeroPagina: int, preco: float) -> None:
        # Atributos.
        self.titulo = titulo 
        self.autor = autor
        self.numeroPagina = numeroPagina
        self.preco = preco
    
    def exibir_dados(self) -> str:
        return f"\nTítulo do livro: {self.titulo} \nAutor do livro: {self.autor} \nNúmero de páginas do livro: {self.numeroPagina} \nPreço do livro: {self.preco}"

# Instanciar classe.
primeiroLivro = Livro("NdL", "AdL", 101, 49.99)
segundoLivro = Livro("NdL 2", "AdL 2", 202, 79.99)

print(primeiroLivro.exibir_dados())
print(segundoLivro.exibir_dados())