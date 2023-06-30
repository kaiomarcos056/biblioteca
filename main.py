from biblioteca_controller import BibliotecaController
from livro import Livro

def exibir_menu():
    print("== Menu ==")
    print("1. Inserir livro")
    print("2. Alterar livro")
    print("3. Deletar livro")
    print("4. Buscar livro")
    print("5. Sair")

def inserir_livro(controller):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    ano_lancamento = int(input("Digite o ano de lançamento do livro: "))
    editora = input("Digite a editora do livro: ")

    livro = Livro(nome, autor, ano_lancamento, editora)
    controller.inserir_livro(livro)
    print("Livro inserido com sucesso!")

def main():
    controller = BibliotecaController()

    while True:
        exibir_menu()
        opcao = input("Digite uma opção: ")

        if opcao == "1":
            inserir_livro(controller)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Resto do código...

if __name__ == "__main__":
    main()
