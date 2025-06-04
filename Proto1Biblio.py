import os
import time

livros = []

def esperar_tecla():
    input("\nPressione Enter para continuar...")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_livro():
    limpar_tela()
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    livro = {
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    }
    livros.append(livro)
    print(f"Livro '{titulo}' adicionado.")
    esperar_tecla()

def listar_livros():
    limpar_tela()
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(livros):
            status = "Disponível" if livro["disponivel"] else "Indisponível"
            print(f"{i+1}. {livro['titulo']} - {livro['autor']} ({status})")
    esperar_tecla()

def emprestar_livro():
    limpar_tela()
    if not livros:
        print("Nenhum livro cadastrado.")
        esperar_tecla()
        return
    listar_livros()
    try:
        indice = int(input("\nNúmero do livro para emprestar: ")) - 1
        if livros[indice]["disponivel"]:
            livros[indice]["disponivel"] = False
            print(f"Livro '{livros[indice]['titulo']}' emprestado com sucesso.")
        else:
            print("Livro já está emprestado.")
    except (ValueError, IndexError):
        print("Entrada inválida.")
    esperar_tecla()

def devolver_livro():
    limpar_tela()
    if not livros:
        print("Nenhum livro cadastrado.")
        esperar_tecla()
        return
    listar_livros()
    try:
        indice = int(input("\nNúmero do livro para devolver: ")) - 1
        if not livros[indice]["disponivel"]:
            livros[indice]["disponivel"] = True
            print(f"Livro '{livros[indice]['titulo']}' devolvido com sucesso.")
        else:
            print("O livro já estava disponível.")
    except (ValueError, IndexError):
        print("Entrada inválida.")
    esperar_tecla()

while True:
    limpar_tela()
    print("=== Sistema de Biblioteca ===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Sair")
    opcao = input("\nEscolha: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        emprestar_livro()
    elif opcao == "4":
        devolver_livro()
    elif opcao == "5":
        print("Saindo...")
        esperar_tecla()
        break
    else:
        print("Opção inválida.")