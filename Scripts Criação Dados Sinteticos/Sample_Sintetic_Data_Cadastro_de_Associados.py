import csv
from faker import Faker
import random

fake = Faker()

# Especifique o caminho do arquivo CSV (caminho relativo)
caminho_arquivo_csv = r"C:\Users\Felipe\Desktop\Script Python SR1\dados_sinteticos_cadastro_de_associados.csv"

with open(caminho_arquivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow([
        "Operadora",
        "Código do Cliente",
        "Razão Social do Cliente",
        "Nome do Associado",
        "Código do Associado",
        "CPF do Titular",
        "Tipo de Participante",
        "Sexo",
        "Plano - Descrição",
        "Data de Nascimento",
        "Data de Admissão do Empregado",
        "Data de Adesão ao Plano",
        "Data de Cancelamento",
        "Estado Civil do Participante",
        "Município do Participante",
        "UF",
        "Contagem Associado Ativo",
        "Operadora - Numero de Registro",
        "Cliente - Grupo (Link)",
        "Cliente - Município",
        "Cliente - UF",
        "Associado - Nome da Mãe",
        "Matricula do Associado",
        "Associado - Bairro",
        "Plano - Código",
        "Plano - Acomodação",
        "CPF Titular",
        "Numero Carteirinha Titular",
        "Nome do Titular",
        "Grupo Familiar",
        "Local Titular"
    ])
    
    for _ in range(1000):  # 1000 linhas de dados sintéticos como exemplo
        operadora = fake.company()
        codigo_cliente = fake.unique.random_int(min=1000, max=9999, step=1)
        razao_social_cliente = fake.company()
        nome_associado = fake.name()
        codigo_associado = fake.unique.random_int(min=10000, max=99999, step=1)
        cpf_titular = fake.unique.ssn()
        tipo_participante = fake.random_element(elements=["Ativo", "Inativo"])
        sexo = fake.random_element(elements=["M", "F"])
        plano_descricao = fake.word(ext_word_list=None)
        data_nascimento = fake.date_of_birth()
        data_admissao_empregado = fake.date_this_century(before_today=True, after_today=False)
        data_adesao_plano = fake.date_this_century(before_today=True, after_today=False)
        data_cancelamento = fake.date_this_century(before_today=True, after_today=False)
        estado_civil_participante = fake.random_element(elements=["Solteiro(a)", "Casado(a)", "Viúvo(a)"])
        municipio_participante = fake.city()
        uf = fake.state_abbr()
        contagem_associado_ativo = random.randint(1, 10)
        operadora_numero_registro = fake.unique.random_int(min=100, max=99999, step=1)
        cliente_grupo_link = fake.url()
        cliente_municipio = fake.city()
        cliente_uf = fake.state_abbr()
        associado_nome_mae = fake.first_name() + " " + fake.last_name()
        matricula_associado = fake.unique.random_int(min=1000, max=99999999, step=1)
        associado_bairro = fake.word(ext_word_list=None)
        plano_codigo = fake.unique.random_int(min=100, max=99999, step=1)
        plano_acomodacao = fake.random_element(elements=["Enfermaria", "Apartamento"])
        cpf_titular = fake.unique.ssn()
        numero_carteirinha_titular = fake.unique.random_int(min=1000, max=99999999, step=1)
        nome_titular = fake.first_name() + " " + fake.last_name()
        grupo_familiar = fake.random_element(elements=["Família A", "Família B", "Família C"])
        local_titular = fake.city()

        writer.writerow([
            operadora,
            codigo_cliente,
            razao_social_cliente,
            nome_associado,
            codigo_associado,
            cpf_titular,
            tipo_participante,
            sexo,
            plano_descricao,
            data_nascimento,
            data_admissao_empregado,
            data_adesao_plano,
            data_cancelamento,
            estado_civil_participante,
            municipio_participante,
            uf,
            contagem_associado_ativo,
            operadora_numero_registro,
            cliente_grupo_link,
            cliente_municipio,
            cliente_uf,
            associado_nome_mae,
            matricula_associado,
            associado_bairro,
            plano_codigo,
            plano_acomodacao,
            cpf_titular,
            numero_carteirinha_titular,
            nome_titular,
            grupo_familiar,
            local_titular
        ])

print(f"Arquivo '{caminho_arquivo_csv}' criado com sucesso com cabeçalhos nas respectivas colunas e codificação UTF-8!")

