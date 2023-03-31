dpi_user = int(input("Digite a DPI do mouse do usuário: "))
peso_user = float(input("Digite o peso em gramas do mouse do usuário: "))


dpi_proplayer = int(input("Digite a DPI do mouse do pro player: "))

peso_proplayer = float(input("Digite o peso em gramas do mouse do pro player: "))

sense_proplayer = float(input("Digite a sensibilidade do CS do pro player: "))

edpi_proplayer = dpi_proplayer*sense_proplayer

peso_relativo = peso_user/peso_proplayer

edpi_relativo = peso_relativo*edpi_proplayer

sense_user = edpi_relativo/dpi_user

print(f"A sensibilidade deve ser ajustada para {sense_user}")
