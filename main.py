# Dados de exemplo
database = {
    "users": [],
    "books": []
}

# Classe para representar usuários
class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.rented_books = []  # Lista de livros alugados

    # Função para adicionar usuário
    def add_user(self):
        if database["users"]:
            ids = [user.id for user in database["users"]]
            new_id = max(ids) + 1
        else:
            new_id = 1

        user = User(new_id, self.name, self.email, self.password)
        database["users"].append(user)
        if new_id > 2:
            print("Usuário cadastrado com sucesso!")

    # Função para alterar dados de usuário
    def update_user(self):
        print(f"\nDados atuais do usuário {self.name}:")
        print(f"ID: {self.id}")
        print(f"Nome: {self.name}")
        print(f"E-mail: {self.email}")
        new_name = input("\nDigite o novo nome (ou deixe em branco para manter o atual): ")
        new_email = input("Digite o novo e-mail (ou deixe em branco para manter o atual): ")
        new_password = input("Digite a nova senha (ou deixe em branco para manter a atual): ")
        if new_name:
            self.name = new_name
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
        print("Dados de usuário atualizados com sucesso!")

    # Função para deletar usuário
    def delete_user(self, logged_user):
        if self == logged_user:
            print("Não é possível deletar o usuário atualmente logado.")
        else:
            database["users"].remove(self)
            print("Usuário deletado com sucesso!")

# Classe para representar livros
class Book:
    def __init__(self, id, titulo, autor, genero, ano, qtd):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano
        self.qtd = int(qtd)

    # Função para adicionar livros
    def add_livro(self):
        if database["books"]:
            ids = [livro.id for livro in database["books"]]
            new_id = max(ids) + 1
        else:
            new_id = 1

        livro = Book(new_id, self.titulo, self.autor, self.genero, self.ano,self.qtd)
        database["books"].append(livro)
        if new_id > 2:
            print("\nLivro cadastrado com sucesso!")

    # Função para alterar dados do livro
    def update_livro(self):
        print(f"\nDados atuais do livro {self.titulo}:")
        print(f"ID: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Genero: {self.genero}")
        print(f"Ano: {self.ano}")
        print(f"Quantidade no estoque: {self.ano}")
        new_titulo = input("\nDigite o novo titulo (ou deixe em branco para manter o atual): ")
        new_autor = input("Digite o novo autor (ou deixe em branco para manter o atual): ")
        new_genero = input("Digite o novo genero (ou deixe em branco para manter a atual): ")
        new_ano = input("Digite o novo ano de lançamento (ou deixe em branco para manter a atual): ")
        new_qtd = input("Digite a quantidade (ou deixe em branco para manter a atual): ")
        if new_titulo:
            self.titulo = new_titulo
        if new_autor:
            self.autor = new_autor
        if new_genero:
            self.genero = new_genero
        if new_ano:
            self.ano = new_ano

        if new_qtd:
            self.qtd = new_qtd
        print("\nDados do livro atualizados com sucesso!")

    # Função para deletar usuário
    def remove_book_by_title(title):
        book_to_delete = None
        for book in database["books"]:
            if book.titulo == title:
                book_to_delete = book
                break

        if book_to_delete:
            print(f"\nLivro encontrado: {book_to_delete.titulo}")
            print(f"Quantidade atual em estoque: {book_to_delete.qtd}")
            quantity = int(input("\nDigite a quantidade de livros a serem removidos: "))

            if quantity > book_to_delete.qtd:
                print("\nQuantidade inválida. Não há livros suficientes no estoque.")
            else:
                book_to_delete.qtd -= quantity

                if book_to_delete.qtd == 0:
                    database["books"].remove(book_to_delete)
                    print("\nLivro removido completamente do estoque.")
                else:
                    print(f"\nQuantidade atualizada em estoque: {book_to_delete.qtd}")

        else:
            print("\nLivro não encontrado.")



# Função para buscar usuários pelo nome
def search_users_by_name(name):
    matching_users = [user for user in database["users"] if name.lower() in user.name.lower()]
    if matching_users:
        print("\nUsuários encontrados:")
        for user in matching_users:
            print(f"ID: {user.id}")
            print(f"Nome: {user.name}")
            print(f"E-mail: {user.email}")
            print("-------------------")
    else:
        print("Nenhum usuário encontrado com esse nome.")

# Função para listar todos os usuários
def list_all_users():
    print("\nUsuários cadastrados:")
    for user in database["users"]:
        print(f"ID: {user.id}")
        print(f"Nome: {user.name}")
        print(f"E-mail: {user.email}")
        print("-------------------")

def list_all_books():
    if database["books"]:
        sorted_books = sorted(database["books"], key=lambda book: book.titulo)
        print("\nLivros cadastrados:")
        for book in sorted_books:
            print(f"ID: {book.id}")
            print(f"Título: {book.titulo}")
            print(f"Autor: {book.autor}")
            print(f"Categoria: {book.genero}")
            print(f"Ano: {book.ano}")
            print(f"Quantidade em estoque: {book.qtd}")
            print("-------------------")
    else:
        print("Nenhum livro cadastrado.")

# Função para exibir o menu de usuários
def show_users_menu():
    print("\nMenu Usuários:")
    print("1. Cadastrar Usuário")
    print("2. Alterar Dados de Usuário")
    print("3. Deletar Usuário")
    print("4. Listar Usuários Cadastrados")
    print("5. Voltar para o Menu Principal\n")

# Função para exibir o menu de livros
def show_livros_menu():
    print("\nMenu Livros:")
    print("1. Cadastrar Livros")
    print("2. Alterar Dados do Livro")
    print("3. Deletar Livro")
    print("4. Listar Livros")
    print("5. Voltar para o Menu Principal\n")

def show_lista_users_menu():
    print("\nSubmenu Usuários:")
    print("1. Listar Todos os Usuários")
    print("2. Buscar Usuário por Nome")
    print("3. Voltar para o Submenu Anterior\n")

def show_lista_livros_menu():
    print("\nSubmenu Livros:")
    print("1. Listar Todos os Livros")
    print("2. Buscar Livro por Titulo")
    print("3. Voltar para o Submenu Anterior\n")

# Função para exibir o menu principal
def show_menu():
    print("\nMenu Principal:")
    print("1. Alugar livro")
    print("2. Devolver livro")
    print("3. Listar livros alugados")
    print("4. Usuários")
    print("5. Livros")
    print("6. Sair\n")


# Função para fazer login
def login(email, password):
    user = next((user for user in database["users"] if user.email == email and user.password == password), None)
    return user


# Adicionar usuário padrão
user = User(None, "Marcos Kaio", "admin", "")
user.add_user()
user = User(None, "Kelvin Erick", "user", "")
user.add_user()

# Adicionar livro padrão
livro = Book(None, "Harry Potter e a Pedra Filosofal", "J. K. Rowling", "Ficção","1997","5")
livro.add_livro()
livro = Book(None, "O Senhor dos Anéis: A Sociedade do Anel", "J. R. R. Tolkien", "Ficção","1954","1")
livro.add_livro()


# Inicio do processo de Login
logged_user = None

while not logged_user:
    email = input("\nDigite seu e-mail: ")
    password = input("Digite sua senha: ")

    logged_user = login(email, password)

    if not logged_user:
        print("Login inválido.")

print(f"\nBem-vindo, {logged_user.name}!")

while True:
    show_menu()
    option = input("Digite o número da opção desejada: ")

    if option == "1":
        # Lógica para alugar livro
        pass
    elif option == "2":
        # Lógica para devolver livro
        pass
    elif option == "3":
        # Lógica para listar livros alugados
        pass
    # Opção Usuario
    elif option == "4":
        while True:
            show_users_menu()
            users_option = input("Digite o número da opção desejada: ")

            if users_option == "1":
                # Opção de Inserir Novo Usuario.
                name = input("\nDigite o nome do usuário: ")
                email = input("Digite o e-mail do usuário: ")
                password = input("Digite a senha do usuário: ")

                user = User(None, name, email, password)
                user.add_user()

            elif users_option == "2":
                # Opção de ALterar os Dados do Usuario.
                email = input("\nDigite o e-mail do usuário: ")

                user = next((user for user in database["users"] if user.email == email), None)
                if user:
                    user.update_user()
                else:
                    print("\nUsuário não encontrado.")

            elif users_option == "3":
                # Opção de Deletar Usuario.
                email = input("\nDigite o e-mail do usuário: ")

                user = next((user for user in database["users"] if user.email == email), None)
                if user:
                    user.delete_user(logged_user)
                else:
                    print("\nUsuário não encontrado.")

            elif users_option == "4":
                while True:
                    show_lista_users_menu()
                    users_option = input("Digite o número da opção desejada: ")

                    if users_option == "1":
                        list_all_users()
                    elif users_option == "2":
                        name = input("Digite o nome do usuário: ")
                        search_users_by_name(name)
                    elif users_option == "3":
                        break
                    else:
                        print("\nOpção inválida. Digite novamente.")

            elif users_option == "5":
                break
            else:
                print("\nOpção inválida. Digite novamente.")

    elif option == "5":

        while True:
            show_livros_menu()
            users_option = input("Digite o número da opção desejada: ")

            if users_option == "1":
                # Opção de Inserir Novo Livro.
                titulo = input("\nDigite o nome do livro: ")
                autor = input("Digite o nome do autor: ")
                genero = input("Digite o gênero: ")
                ano = input("Digite o ano de lançamento: ")
                qtd = input("Digite a quantidade em estoque: ")

                livro = Book(None, titulo, autor, genero, ano,qtd)
                livro.add_livro()

            elif users_option == "2":
                # Opção de ALterar os Dados do Livro.
                titulo = input("\nDigite o titulo do livro: ")

                book = next((book for book in database["books"] if book.titulo == titulo), None)
                if book:
                    book.update_livro()
                else:
                    print("\nLivro não encontrado.")

            elif users_option == "3":
                # Opção de Deletar Livro.
                title = input("\nDigite o título do livro a ser removido: ")
                Book.remove_book_by_title(title)

            elif users_option == "4":
                while True:
                    show_lista_livros_menu()
                    users_option = input("Digite o número da opção desejada: ")

                    if users_option == "1":
                        list_all_books()
                    elif users_option == "2":
                        pass
                    elif users_option == "3":
                        break
                    else:
                        print("\nOpção inválida. Digite novamente.")

            elif users_option == "5":
                break
            else:
                print("\nOpção inválida. Digite novamente.")

    elif option == "6":
        print("\nSaindo do sistema...")
        break
    else:
        print("\nOpção inválida. Digite novamente.")
