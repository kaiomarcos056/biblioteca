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

# Classe para representar livros
class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

# Função para adicionar usuário
def add_user(name, email, password):
    if database["users"]:
        ids = [user.id for user in database["users"]]
        new_id = max(ids) + 1
    else:
        new_id = 1

    user = User(new_id, name, email, password)
    database["users"].append(user)
    print("Usuário cadastrado com sucesso!")

# Função para alterar dados de usuário
def update_user(email):
    user = next((user for user in database["users"] if user.email == email), None)
    if user:
        print(f"Dados atuais do usuário {user.name}:")
        print(f"ID: {user.id}")
        print(f"Nome: {user.name}")
        print(f"E-mail: {user.email}")
        new_name = input("Digite o novo nome (ou deixe em branco para manter o atual): ")
        new_email = input("Digite o novo e-mail (ou deixe em branco para manter o atual): ")
        if new_name:
            user.name = new_name
        if new_email:
            user.email = new_email
        print("Dados de usuário atualizados com sucesso!")
    else:
        print("Usuário não encontrado.")

# Função para deletar usuário
def delete_user(email):
    user = next((user for user in database["users"] if user.email == email), None)
    if user:
        database["users"].remove(user)
        print("Usuário deletado com sucesso!")
    else:
        print("Usuário não encontrado.")

# Função para listar usuários cadastrados
def list_users():
    print("Usuários cadastrados:")
    for user in database["users"]:
        print(f"ID: {user.id}")
        print(f"Nome: {user.name}")
        print(f"E-mail: {user.email}")
        print("-------------------")


# Função para buscar usuários pelo nome
def search_users_by_name(name):
    matching_users = [user for user in database["users"] if name.lower() in user.name.lower()]
    if matching_users:
        print("Usuários encontrados:")
        for user in matching_users:
            print(f"ID: {user.id}")
            print(f"Nome: {user.name}")
            print(f"E-mail: {user.email}")
            print("-------------------")
    else:
        print("Nenhum usuário encontrado com esse nome.")

# Função para listar todos os usuários
def list_all_users():
    print("Usuários cadastrados:")
    for user in database["users"]:
        print(f"ID: {user.id}")
        print(f"Nome: {user.name}")
        print(f"E-mail: {user.email}")
        print("-------------------")

# Função para exibir o menu de usuários
def show_users_menu():
    print("Menu Usuários:")
    print("1. Cadastrar Usuário")
    print("2. Alterar Dados de Usuário")
    print("3. Deletar Usuário")
    print("4. Listar Usuários Cadastrados")
    print("5. Voltar para o Menu Principal")
    print("\n")

def show_lista_users_menu():
    print("Submenu Usuários:")
    print("1. Listar Todos os Usuários")
    print("2. Buscar Usuário por Nome")
    print("3. Voltar para o Submenu Anterior")
    print("\n")

# Função para exibir o menu principal
def show_menu():
    print("Menu Principal:")
    print("1. Alugar livro")
    print("2. Devolver livro")
    print("3. Listar livros alugados")
    print("4. Usuários")
    print("5. Sair")
    print("\n")

# Função para fazer login
def login(email, password):
    user = next((user for user in database["users"] if user.email == email and user.password == password), None)
    return user

# Adicionar usuário
add_user("John Doe", "admin", "")
add_user("Jane Smith", "jane@example.com", "password456")

# Solicitar login
email = input("Digite seu e-mail: ")
password = input("Digite sua senha: ")

logged_user = login(email, password)

if logged_user:
    print(f"Bem-vindo, {logged_user.name}!")
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
        elif option == "4":
            while True:
                show_users_menu()
                users_option = input("Digite o número da opção desejada: ")

                if users_option == "1":

                    name = input("Digite o nome do usuário: ")
                    email = input("Digite o e-mail do usuário: ")
                    password = input("Digite a senha do usuário: ")
                    add_user(name, email, password)

                elif users_option == "2":

                    email = input("Digite o e-mail do usuário: ")
                    update_user(email)

                elif users_option == "3":

                    email = input("Digite o e-mail do usuário: ")
                    delete_user(email)

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
                            print("Opção inválida. Digite novamente.")

                elif users_option == "5":
                    break
                else:
                    print("Opção inválida. Digite novamente.")
        elif option == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Digite novamente.")
else:
    print("Login inválido.")
