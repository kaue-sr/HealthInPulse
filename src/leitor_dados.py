import csv

caminho_arquivo = "dados/dados_pulseira.csv"

with open(caminho_arquivo, mode='r', newline='') as arquivo:
    leitor = csv.DictReader(arquivo)

    print("Dados da pulseira:")
    print("------------------------------------------------------------")
    print("Hora | Temperatura | Frequência Cardíaca | Pressão Arterial | Oxigenação | Horas de Sono")
    print("------------------------------------------------------------")
    for linha in leitor:
        print(f"{linha['data_hora']} |{linha['temperatura']}°C |{linha['frq_cardiaca']:>3} bpm |{linha['pressao_sistolica']:>3}/{linha['pressao_diastolica']:>3} mmHg |{linha['oxigenacao']:>5}% |{linha['horas_sono']:>3}h")