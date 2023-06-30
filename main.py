from biblioteca_controller import BibliotecaController
from livro import Livro

# Criar uma instância do BibliotecaController
biblioteca_controller = BibliotecaController()

# Criar alguns livros
livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "Editora A")
livro2 = Livro("1984", "George Orwell", 1949, "Editora B")

# Inserir livros no DataFrame
biblioteca_controller.inserir_livro(livro1)
biblioteca_controller.inserir_livro(livro2)

# Imprimir o DataFrame de livros
print(biblioteca_controller.df_livros)

# Resto do código...
