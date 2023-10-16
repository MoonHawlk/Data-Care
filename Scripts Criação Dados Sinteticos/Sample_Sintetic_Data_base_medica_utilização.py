import csv
from faker import Faker
import random

fake = Faker()

# Especifique o caminho do arquivo CSV (caminho relativo)
caminho_arquivo_csv = r"C:\Users\Felipe\Desktop\Script Python SR1\dados_sinteticos_base_medica_utilização.csv"

with open(caminho_arquivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow([
        "Operadora", "Código do Cliente", "Razão Social do Cliente",
        "Código do Associado", "Nome do Associado", "Tipo de Associado",
        "Sexo", "Data de Nascimento", "Grupo Tipo de Atendimento",
        "Valor", "Data do Atendimento", "Competência", "CGC do Prestador Local",
        "Nome do Prestador Local", "Especialidade - Descrição", "Prestador Local Próprio",
        "Cidade do Prestador Local", "Estado do Prestador Local", "Código do Procedimento",
        "Nome do Procedimento", "Código do CID", "Qtd Procedimentos", "Cód do Grupo de Contrato",
        "Plano - Código", "Plano - Descrição", "GUIA", "Especialidade - Codigo",
        "Classe de procedimento", "Grupo Familiar", "CPF Titular", "Carteirinha Titular",
        "Nome Titular"
    ])
    
    for _ in range(1000):  # 1000 linhas de dados sintéticos como exemplo
        operadora = random.choice(["A","B","C","D"])
        codigo_cliente = fake.random_int(1000, 9999)
        razao_social_cliente = fake.company()
        codigo_associado = fake.random_int(10000, 99999)
        nome_associado = fake.name()
        tipo_associado = fake.word()
        sexo = fake.random_element(["M", "F"])
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=75)
        grupo_tipo_atendimento = fake.word()
        valor = random.uniform(100, 100000)
        data_atendimento = fake.date_this_century(before_today=True, after_today=False)
        competencia = fake.month_name() + " " + fake.year()
        cgc_prestador_local = fake.random_int(10000000, 99999999)
        nome_prestador_local = fake.company()
        especialidade_descricao = fake.word()
        prestador_local_proprio = fake.random_element(["Sim", "Não"])
        cidade_prestador_local = fake.city()
        estado_prestador_local = fake.state_abbr()
        codigo_procedimento = fake.random_int(100, 999)
        nome_procedimento = fake.word()
        codigo_cid = fake.random_element(["A00", "B01", "C02", "D03"])
        qtd_procedimentos = random.randint(1, 5)
        cod_grupo_contrato = fake.random_int(1, 10)
        plano_codigo = fake.random_int(100, 999)
        plano_descricao = fake.word()
        guia = fake.random_int(10000, 99999)
        especialidade_codigo = fake.random_int(1000, 9999)
        classe_procedimento = fake.random_element(["A", "B", "C"])
        grupo_familiar = fake.random_element(["Sim", "Não"])
        cpf_titular = fake.unique.ssn()
        carteirinha_titular = fake.random_int(100000, 999999)
        nome_titular = fake.name()

        # Escreva os dados na linha do arquivo CSV
        writer.writerow([
            operadora, codigo_cliente, razao_social_cliente, codigo_associado, nome_associado, tipo_associado,
            sexo, data_nascimento, grupo_tipo_atendimento, valor, data_atendimento, competencia, cgc_prestador_local,
            nome_prestador_local, especialidade_descricao, prestador_local_proprio, cidade_prestador_local,
            estado_prestador_local, codigo_procedimento, nome_procedimento, codigo_cid, qtd_procedimentos,
            cod_grupo_contrato, plano_codigo, plano_descricao, guia, especialidade_codigo, classe_procedimento,
            grupo_familiar, cpf_titular, carteirinha_titular, nome_titular
        ])

#print(f"Arquivo '{caminho_arquivo_csv}' criado com sucesso com cabeçalhos nas respectivas colunas e codificação UTF-8!")
