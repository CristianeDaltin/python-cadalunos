#util/validacao.py
"""
#Responsabilidade única: validar dados de entrada do usuario
Nenhuma lógica de hanela, bamco ou calculo entra aui.
"""

def validar_nome(nome: str) ->str:
    """
    valida se o nome nao está vazio:
    Retorna o nome sem espaço extras
    Levanta uma Exceção se a validação estiver inválida
    """
    nome = nome.strip() #elimina espaçoes extras    #Paulo Oliveira
    if not nome:
        raise ValueError("O nome não pode estar vazio.")
    
    return nome

def validar_nota(valor_str: str, campo: str = "Nota") -> float:
    """
    Valida se uma strig representa uma nota entre  0 e 10.
    Retorna o float (nimero decimal)
    Levanta um a exceção se não estiver no intervalo
    """
    try:
        nota = float(valor_str)

    except ValueError:
        raise ValueError(f"{campo}:'{valor_str}' não é o unico válido. Ex7.5")
                         
    if not 0 <= nota <= 10:
        raise ValueError(f"{campo}: o valor '{valor_str}'está fora do intervalo")
    return nota
    
def validar_cep(cep: str) -> str:       
    """
    Validar  o formato básico do CEP (somente 8 dígitos, 8 caracteres).
    Retorna o CEP sem traço
    Levanta uma exceção se  formato for inválido.
    """
    cep = cep.strip().replace("-","")
    if not cep.isdigit() or len(cep) != 8:
        
        raise ValueError(f"CEP{cep} invalido. Use o formato: 12345-678")
    
    return cep
