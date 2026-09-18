from datetime import datetime
import csv
import os

def executar_checkup():
    #Tudo aqui dentro só vai rodar quando alguém chama a função
    print("=======================================")
    print("BEM-VINDO AO CHECK-UP DIGITAL (TRIAGEM)")
    print("=======================================")
    print("Responda com '0' para 'não' e '1' para 'sim', ou digite os valores solicitados.\n")

    # 1. Capturar data e hora atual do sistema
    data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # --- DOR NO PEITO ---
    while True:
        dor_no_peito = input("Você está sentindo dor no peito? (0/1): ")
        if dor_no_peito in ['0', '1']:
            break
        print("Entrada inválida. Por favor, insira apenas '0' ou '1'.")

    intensidade_dor = '0'
    if dor_no_peito == '1':
        while True:
            try:
                valor = int(input("Qual a intensidade da dor no peito de 0 a 10? (0 = sem dor, 10 = insuportável): "))
                if 0 <= valor <= 10:
                    intensidade_dor = str(valor)
                    break
                print("Erro: digite um número entre 0 e 10.")
            except ValueError:
                print("Erro: digite apenas números inteiros.")

    # --- FALTA DE AR ---
    while True:
        falta_de_ar = input("Você está sentindo falta de ar? (0/1): ")
        if falta_de_ar in ['0', '1']:
            break
        print("Entrada inválida. Por favor, insira apenas '0' ou '1'.")

    intensidade_falta_ar = '0'
    if falta_de_ar == '1':
        while True:
            try:
                valor = int(input("Qual a intensidade da falta de ar de 0 a 10? (0 = sem falta de ar, 10 = insuportável): "))
                if 0 <= valor <= 10:
                    intensidade_falta_ar = str(valor)
                    break
                print("Erro: digite um número entre 0 e 10.")
            except ValueError:
                print("Erro: digite apenas números inteiros.")

    # --- FEBRE ---
    while True:
        febre = input("Você está com febre? (0/1): ")
        if febre in ['0', '1']:
            break
        print("Entrada inválida. Por favor, insira apenas '0' ou '1'.")

    temperatura = '0'
    if febre == '1':
        while True:
            try:
                valor = float(input("Qual a sua temperatura atual em °C? (Ex: 37.5): "))
                if 30.0 <= valor <= 45.0:
                    temperatura = str(valor)
                    break
                print("Erro: digite uma temperatura corporal válida (entre 30.0 e 45.0).")
            except ValueError:
                print("Erro: digite um número válido.")

    # --- QUALIDADE DO SONO ---
    while True:
        try:
            qualidade_do_sono = int(input("Como você avalia a qualidade do seu sono de 0 a 10? (0 = péssimo, 10 = excelente): "))
            if 0 <= qualidade_do_sono <= 10:
                qualidade_do_sono = str(qualidade_do_sono)
                break
            print("Erro: digite um número entre 0 e 10.")
        except ValueError:
            print("Erro: você digitou um caractere inválido. Insira um número.")

    # --- NÍVEL DE ESTRESSE ---
    while True:
        try:
            nivel_de_estresse = int(input("Como você avalia o seu nível de estresse de 0 a 10? (0 = sem estresse, 10 = extremo): "))
            if 0 <= nivel_de_estresse <= 10:
                nivel_de_estresse = str(nivel_de_estresse)
                break
            print("Erro: digite um número entre 0 e 10.")
        except ValueError:
            print("Erro: você digitou um caractere inválido. Insira um número.")

    # 2. Estruturando os dados em um Dicionário
    dados_sessao = {
        "data_hora": data_hora_atual,
        "dor_no_peito": dor_no_peito,
        "intensidade_dor_peito": intensidade_dor,
        "falta_de_ar": falta_de_ar,
        "intensidade_falta_ar": intensidade_falta_ar,
        "febre": febre,
        "temperatura": temperatura,
        "qualidade_sono": qualidade_do_sono,
        "nivel_estresse": nivel_de_estresse
    }

    # 3. Salvando no CSV com o modo 'append' ('a')
    caminho_pasta = "dados"
    caminho_arquivo = os.path.join(caminho_pasta, "dados_triagem.csv")

    # Garante que a pasta 'dados' existe antes de salvar
    os.makedirs(caminho_pasta, exist_ok=True)

    # Verifica se o arquivo já existe e se está vazio para decidir sobre o cabeçalho
    arquivo_existe = os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0

    with open(caminho_arquivo, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        campos = list(dados_sessao.keys())
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

        # Se o arquivo não existe ou está vazio, escreve o cabeçalho primeiro
        if not arquivo_existe:
            escritor.writeheader()

        escritor.writerow(dados_sessao)

    print("\nCheck-up finalizado e salvo com sucesso em 'dados/dados_triagem.csv'!")

if __name__ == "__main__":
    executar_checkup()
#Sintomar para a triagem

#Colunas Binárias

##Cardiorrespiratórios

###Dor no peito
###Falta de ar
###Palpitações
###Tosse
#-----------------
##Neurológicos
###Dor de cabeça
###Tontura
###Visão turva
###Confusão mental
###Desmaio ou quase desmaio
#-----------------
##Gastrointestinais
###Náusea 
###Vômito
###Diarreia
###Dor abdominal
#-----------------
##Musculoesqueléticos
###Dor nas articulações
###Dor muscular
###Dormência ou formigamento
#-----------------
##Gerias/Sistêmicos
###Febre
###Fadiga
###Calafrios
###Sudorese excessiva
###Inchaço nas pernas/tornozelos
###Sede excessiva
###Perda ou ganho de peso recente
#-----------------

# Perguntas de histórico/hábitos de saúde
## Uso de medicamentos contínuos(sim/não + qual, se quiser manter texto livre por enquanto)
##Doenças pré-existentes / diagnosticadas (sim/não + qual)
##Histórico familiar de doenças cardíacas (sim/não) — esse é um fator de risco clássico em modelos de saúde
##Fumante (sim/não)
##Consumo de álcool (frequência, ou simplifique pra sim/não por enquanto)
#-----------------

#Escalas (0 a 10)
##Qualidade do sono
##Nível de estresse
##Intensidade da dor (se marcou "sim" em alguma dor, quanto dói de 0 a 10 — isso é bem usado em triagem real)
##Nível de energia / disposição no dia

