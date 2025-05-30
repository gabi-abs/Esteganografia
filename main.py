from esteganografia import codificar, decodificar


def principal():
    """Função principal para interação com o usuário."""
    escolha = input(":: Bem-vindo à Esteganografia ::\n1. Codificar\n2. Decodificar\nEscolha uma opção: ")
    if escolha == '1':
        codificar()
    elif escolha == '2':
        print("Mensagem Decodificada: " + decodificar())
    else:
        print("Escolha inválida. Encerrando o programa.")

if __name__ == "__main__":
    principal()