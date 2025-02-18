import os;

def mostraNome():
    print("------------------")
    print("Bem vindo à IPido")
    print("------------------\n")

def mostraOpcoes():
    print("1. Cadastrar Restaurante\n")
    print("2. Listar Restaurante\n")
    print("3. Ativar restaurante\n")
    print("4. Sair\n")

opcaoSelecionada = int(input("Escolha uma opção: "))
print(f'Opção: {opcaoSelecionada}')

def cadastrarRestaurante():
    nomeRestaurante = input("Digite o nome do seu restaurante: ")
    senha = input("Digite a senha do seu restaurante: ")
    return nomeRestaurante, senha

def listarRestaurante():
    print("Listado")

def ativarRestaurante():
    print("Ativado")

def finalizarAPP():
    os.system("cls")
    print("Bye")

def main():
    mostraNome()
    mostraOpcoes()


if opcaoSelecionada == 1:
    cadastrarRestaurante()
elif opcaoSelecionada == 2:
    listarRestaurante()
elif opcaoSelecionada == 3:
    ativarRestaurante()
else:
    finalizarAPP()

if __name__ == '__main__':
    main()