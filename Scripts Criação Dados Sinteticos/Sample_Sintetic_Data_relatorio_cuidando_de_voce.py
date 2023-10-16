import csv
from faker import Faker
import random

fake = Faker()

# Especifique o caminho do arquivo CSV (caminho relativo)
caminho_arquivo_csv = r"C:\Users\Felipe\Desktop\Script Python SR1\dados_sinteticos_relatorio_cuidando_de_voce.csv"

with open(caminho_arquivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow([
        "SequentialId", "Status", "StorageDate", "CloseDate", "Team", "Closed", "Tags",
        "QueueTime", "FirstResponseTime", "AverageResponseTime", "CustomerName", "AgentName",
        "AgentEmail", "Tipo", "Empresa", "Apolice", "Plano", "QUESTÃO 1", "QUESTÃO 2"
    ])
    
    for _ in range(1000):  # 1000 linhas de dados sintéticos como exemplo
        sequential_id = fake.uuid4()
        status = random.choice(["Open", "Closed", "Pending"])
        storage_date = fake.date_of_birth(minimum_age=18, maximum_age=75)
        close_date = fake.date_between_dates(storage_date)
        team = fake.company()
        closed = random.choice(["Yes", "No"])
        tags = fake.words(nb=random.randint(1, 5))
        queue_time = random.randint(1, 60)
        first_response_time = random.randint(5, 30)
        average_response_time = random.uniform(1.0, 10.0)
        customer_name = fake.name()
        agent_name = fake.name()
        agent_email = fake.email()
        tipo = random.choice(["Type1", "Type2", "Type3"])
        empresa = fake.company()
        apolice = fake.random_int(min=1000, max=99999999999)
        plano = random.choice(["Platinum", "Gold", "Silver", "Bronze"])
        questao1 = fake.sentence()
        questao2 = fake.sentence()

        writer.writerow([
            sequential_id, status, storage_date, close_date, team, closed, tags, queue_time,
            first_response_time, average_response_time, customer_name, agent_name, agent_email,
            tipo, empresa, apolice, plano, questao1, questao2
        ])

print(f"Arquivo '{caminho_arquivo_csv}' criado com sucesso com cabeçalhos nas respectivas colunas e codificação UTF-8!")

