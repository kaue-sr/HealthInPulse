import csv
import random
from datetime import datetime, timedelta

#Definindo as colunas do arquivo CSV
colunas = ["data_hora" , "temperatura", "frq_cardiaca", "pressao_sistolica", "pressao_diastolica", "oxigenacao", "horas_sono"]

#Indicando o caminho para o arquivo CSV
caminho_arquivo = "dados/dados_pulseira.csv"

#Definindo a hora e data atual
data_atual = datetime.now()

with open(caminho_arquivo, mode='w', newline='') as arquivo_csv:
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
    escritor.writeheader()

    for i in range(100):
        data_hora = data_atual

        if i%10 == 0:
            temperatura = round(random.uniform(38.0, 40.0), 1)
            frq_cardiaca = random.randint(120, 180)
            pressao_sistolica = random.randint(140, 180)
            pressao_diastolica = random.randint(90, 120)
            oxigenacao = round(random.uniform(85.0, 95.0), 1)
            horas_sono = random.randint(2, 4)
        else:
            temperatura = round(random.uniform(36.0, 37.5), 1)
            frq_cardiaca = random.randint(60, 100)
            pressao_sistolica = random.randint(90, 120)
            pressao_diastolica = random.randint(60, 80)
            oxigenacao = round(random.uniform(95.0, 100.0), 1)
            horas_sono = random.randint(6, 9)

        linha = {
            "data_hora": data_hora.strftime("%Y-%m-%d %H:%M:%S"),
            "temperatura": temperatura,
            "frq_cardiaca": frq_cardiaca,
            "pressao_sistolica": pressao_sistolica,
            "pressao_diastolica": pressao_diastolica,
            "oxigenacao": oxigenacao,
            "horas_sono": horas_sono,
        }

        escritor.writerow(linha)

        data_atual = data_atual + timedelta(minutes=1)

