print("------------------")
print("Bem vindo à IPido")
print("------------------\n")

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

if opcaoSelecionada == 1:
    cadastrarRestaurante()
elif opcaoSelecionada == 2:
    listarRestaurante()
elif opcaoSelecionada == 3:
    ativarRestaurante()
else:
    print("BYE")
    exit()

