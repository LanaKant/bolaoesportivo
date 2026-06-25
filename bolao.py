import random

arquivo_selecoes = "selecoes_copa_2026.txt"

selecoes_lista = [
    "África do Sul", "Alemanha", "Arábia Saudita", "Argélia", "Argentina", "Austrália", "Áustria", 
    "Bélgica", "Bósnia e Herzegovina", "Brasil", "Cabo Verde", "Canadá", "Catar", "Colômbia", 
    "Coreia do Sul", "Costa do Marfim", "Croácia", "Curaçao", "Egito", "Equador", "Escócia", 
    "Espanha", "Estados Unidos", "França", "Gana", "Haiti", "Holanda", "Inglaterra", "Irã", 
    "Iraque", "Japão", "Jordânia", "Marrocos", "México", "Noruega", "Nova Zelândia", "Panamá", 
    "Paraguai", "Portugal", "República Democrática do Congo", "República Tcheca", "Senegal", 
    "Suécia", "Suíça", "Tunísia", "Turquia", "Uruguai", "Uzbequistão"
]

with open(arquivo_selecoes, "w", encoding="utf-8") as f:
    for s in selecoes_lista:
        f.write(s + "\n")

selecoes = []

with open(arquivo_selecoes, "r", encoding="utf-8") as f:
    for linha in f:
        selecoes.append(linha.strip())

print("=" *40)
print("BOLÃO DA COPA DO MUNDO 2026")
print("=" *40)

palpites_dos_usuarios = {}

while True:
    nome = input("\nNome do participante (ou digite 'sair' para encerrar): ").strip()

    if nome.lower() == 'sair':
        break

    print("\nDigite suas apostas para o Top 3 da Copa:\n")

    campeao = input("\t1º Lugar (Campeão): ").strip()
    vice = input("\t2º Lugar (Vice): ").strip()
    terceiro = input("\t3º Lugar: ").strip()

    palpites_dos_usuarios[nome] = [campeao, vice, terceiro]

    print(f"\nPalpite de {nome} registrado com sucesso!")

if not palpites_dos_usuarios:
    print("Nenhum palpite foi registrado. Encerrando o programa.")
else:
    print("\n" + "=" *40)
    print("SIMULANDO OS RESULTADOS DA COPA...")
    print("=" *40 + "\n")

    resultado_oficial = random.sample(selecoes, 3)

    print(f"Campeão: {resultado_oficial[0]}")
    print(f"Vice-campeão: {resultado_oficial[1]}")
    print(f"3º Lugar: {resultado_oficial[2]}")

    lista_ranking = []

    for usuario, palpites in palpites_dos_usuarios.items():
        pontos = 0

        if palpites[0].lower() == resultado_oficial[0].lower():
            pontos += 3
        elif palpites[0].lower() == resultado_oficial[1].lower() or palpites[0].lower() == resultado_oficial[2].lower():
            pontos += 1

        if palpites[1].lower() == resultado_oficial[1].lower():
            pontos += 3
        elif palpites[1].lower() == resultado_oficial[0].lower() or palpites[1].lower() == resultado_oficial[2].lower():
            pontos += 1

        if palpites[2].lower() == resultado_oficial[2].lower():
            pontos += 3
        if palpites[2].lower() == resultado_oficial[0].lower() or palpites[2].lower() == resultado_oficial[1].lower():
            pontos += 1

        lista_ranking.append([pontos, usuario])

    lista_ranking.sort(reverse=True)

    nome_arquivo = "resultado_bolao_2026.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("=== RESULTADO OFICIAL DA COPA 2026 ===\n")
        arquivo.write(f"1º Lugar: {resultado_oficial[0]}\n")
        arquivo.write(f"2º Lugar: {resultado_oficial[1]}\n")
        arquivo.write(f"3º Lugar: {resultado_oficial[2]}\n\n")

        arquivo.write("=== RANKING DOS PARTICIPANTES ===\n")

        posicao = 1

        for item in lista_ranking:
            pontos = item[0]
            usuario = item[1]
            palpite = palpites_dos_usuarios[usuario]

            arquivo.write(f"{posicao}º | {usuario} - {pontos} pontos\n")
            arquivo.write(f"\tPalpite: 1º {palpite[0]}, 2º {palpite[1]}, 3º {palpite[2]}\n\n")

            posicao += 1

    print("\nO ranking e os resultados foram salvos no arquivo: " + nome_arquivo)
