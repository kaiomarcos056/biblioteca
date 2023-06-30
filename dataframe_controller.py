import pandas as pd

class DataFrameController:
    def __init__(self):
        self.df_livros = pd.DataFrame(columns=['Nome', 'Autor', 'Ano de Lançamento', 'Editora'])

    def inserir_livro(self, livro):
        novo_livro = {
            'Nome': livro.nome,
            'Autor': livro.autor,
            'Ano de Lançamento': livro.ano_lancamento,
            'Editora': livro.editora
        }
        self.df_livros = self.df_livros.append(novo_livro, ignore_index=True)

    def alterar_livro(self, livro, novo_nome, novo_autor, novo_ano_lancamento, nova_editora):
        filtro = self.df_livros['Nome'] == livro.nome
        self.df_livros.loc[filtro, 'Nome'] = novo_nome
        self.df_livros.loc[filtro, 'Autor'] = novo_autor
        self.df_livros.loc[filtro, 'Ano de Lançamento'] = novo_ano_lancamento
        self.df_livros.loc[filtro, 'Editora'] = nova_editora

    def buscar_livro(self, nome):
        filtro = self.df_livros['Nome'] == nome
        livro_encontrado = self.df_livros.loc[filtro]
        if livro_encontrado.empty:
            return None
        return Livro(livro_encontrado['Nome'].values[0],
                     livro_encontrado['Autor'].values[0],
                     livro_encontrado['Ano de Lançamento'].values[0],
                     livro_encontrado['Editora'].values[0])
