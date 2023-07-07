import pandas as pd


class BibliotecaController:
    def __init__(self):
        self.df_livros = pd.DataFrame(columns=['Nome', 'Autor', 'Ano de Lançamento', 'Editora'])

    def inserir_livro(self, livro):
        novo_livro = pd.DataFrame([[livro.nome, livro.autor, livro.ano_lancamento, livro.editora]],
                                  columns=['Nome', 'Autor', 'Ano de Lançamento', 'Editora'])
        self.df_livros = pd.concat([self.df_livros, novo_livro], ignore_index=True)

        self.exibir_detalhes_livro(novo_livro)

    def exibir_detalhes_livro(self, livro):
        print("Detalhes do livro inserido:")
        print("Nome:", livro['Nome'].values[0])
        print("Autor:", livro['Autor'].values[0])
        print("Ano de Lançamento:", livro['Ano de Lançamento'].values[0])
        print("Editora:", livro['Editora'].values[0])
        print()

    def mostrar_livros(self):
        print("Lista de livros:")
        print(self.df_livros)
        print()

    # Resto do código...
