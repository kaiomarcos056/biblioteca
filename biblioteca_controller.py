import pandas as pd

class BibliotecaController:
    def __init__(self):
        self.df_livros = pd.DataFrame(columns=['Nome', 'Autor', 'Ano de Lançamento', 'Editora'])

    def inserir_livro(self, livro):
        novo_livro = pd.DataFrame([[livro.nome, livro.autor, livro.ano_lancamento, livro.editora]],
                                  columns=['Nome', 'Autor', 'Ano de Lançamento', 'Editora'])
        self.df_livros = pd.concat([self.df_livros, novo_livro], ignore_index=True)

    # Resto do código...
