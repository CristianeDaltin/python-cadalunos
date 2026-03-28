from util.validacao import validar_nome, validar_nota, validar_cep
from util.cep import buscar_endereco
from util.calculos import media, aprovado
from util.banco import inserir_registro

def cadastrar_aluno_cli():
    """
    conduz o cadastro de um aluno pelo terminal. 
    Valida cada campo antes de prosseguir.

    """
    print("\n=== Cadastro de Aluno ===\n")
    while True:
        try:
            nome = validar_nome(input("Digite o nome do aluno: "))
            break
        except ValueError as e:
            print(f"{e}")

    while True:
        try:
            n1 = validar_nota(input("Digita a Nota 1: "), campo = "Nota 1")
            break
        except ValueError as e:
            print(f"{e}")

    while True:
        try:
            n2 = validar_nota(input("Digita a Nota 2: "), campo = "Nota 2")
            break
        except ValueError as e:
            print(f"{e}")

    #leitura e validacao do CEP
    while True:
        try:
            cep = validar_cep(input("Digite o CEP do aluno: "))
        except ValueError as e:
            print(f"{e}")
            continue

        endereco = buscar_endereco(cep)
        if endereco:
            print(f"{endereco ['rua']} - {endereco['cidade']}/{endereco['estado']}")
            break 
        else:
            print("👍CEP nao encontrado. Tente novamente.")

            numero = input("Digite o numero do Endereço (Enter para S/N: ").strip()

    #---Processar a Regra de Negócio ---
    m = media(n1,n2)
    status = aprovado(m)

    #---Persistir os Dados no Banco---
    #inserir_registro(nome, n1,n2)

def listar_alunos_cli() -> None:
    """ Exibir todos os alunos cadastrados no terminal"""
    #ToDo

def iniciar() -> None:
    #ciar_tabela()
    cadastrar_aluno_cli()
    #listrar_alunos_cli()

            


    