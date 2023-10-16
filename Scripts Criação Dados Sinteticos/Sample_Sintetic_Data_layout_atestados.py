import csv
from faker import Faker
import random

fake = Faker()

# Especifique o caminho do arquivo CSV (caminho relativo)
caminho_arquivo_csv = r"C:\Users\Felipe\Desktop\Script Python SR1\dados_sinteticos_layout_atestados.csv"

with open(caminho_arquivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(["NOME FUNCIONARIO", "CPF", "DATA", "UNIDADE ATENDIMENTO", "NOME PRESCRITOR", "CRM", "UF CR", "TIPO CR", "TEMPO", "TIPO TEMPO", "HORAENTRADA", "HORASAIDA", "CID", "ACEITO", "OBSEVAÇAO", "ORIGEM", "RECEPCAO", "ESPECIALIDADE"])
    
    for _ in range(1000):  # 1000 linhas de dados sintéticos como exemplo
        nome_funcionario = fake.name()
        cpf = fake.unique.ssn()
        data = fake.date_of_birth()
        unidade_atendimento = fake.company()
        nome_prescritor = fake.name()
        crm = fake.unique.random_int(min=10000, max=99999, step=1)
        uf_cr = fake.state_abbr()
        tipo_cr = fake.random_element(elements=["A", "B", "C"])
        tempo = random.randint(1, 30)
        tipo_tempo = fake.random_element(elements=["Dias", "Meses", "Anos"])
        hora_entrada = fake.time(pattern='%H:%M:%S', end_datetime=None)
        hora_saida = fake.time(pattern='%H:%M:%S', end_datetime=None)
        cid = fake.random_element(elements=["A00", "B01", "C02"])
        aceito = fake.random_element(elements=["Sim", "Não"])
        observacao = fake.text()
        origem = fake.random_element(elements=["Hospital", "Clínica", "Pronto-Socorro"])
        recepcao = fake.random_element(elements=["Recepção A", "Recepção B", "Recepção C"])
        especialidade = fake.random_element(elements=["Cardiologia", "Ortopedia", "Pediatria"])

        writer.writerow([nome_funcionario, cpf, data, unidade_atendimento, nome_prescritor, crm, uf_cr, tipo_cr, tempo, tipo_tempo, hora_entrada, hora_saida, cid, aceito, observacao, origem, recepcao, especialidade])

print(f"Arquivo '{caminho_arquivo_csv}' criado com sucesso com cabeçalhos nas respectivas colunas e codificação UTF-8!")

