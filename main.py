from util import media, aprovado, mensagem
from util import criar_tabela, inserir_registro, listar_registros

criar_tabela()

nome_aluno = input("Olá, espero que esteja bem! Por favor, digite o nome completo do aluno que gostaria de registrar a nota: ").upper() 
print(f"Ótimo, {nome_aluno}! Agora vamos registrar as notas do aluno." )
print("\n")
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

media = media(n1, n2) 
status = aprovado(media)

#salvar aluno no banco
inserir_registro(nome_aluno, n1, n2)

#listar os registros
for aluno in listar_registros():
    print(aluno)
