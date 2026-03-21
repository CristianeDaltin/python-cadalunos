def mensagem(nome, media, status):
    if status == "Aprovado":
        return f"{nome}, você foi aprovado com média final {media:.2f}"
    else:
        return f"{nome}, você foi reprovado com média final {media:.2f}"