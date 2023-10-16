import csv
from faker import Faker
import random

fake = Faker()

# Especifique o caminho do arquivo CSV (caminho relativo)
caminho_arquivo_csv = r"C:\Users\totov\OneDrive\Área de Trabalho\Data-Care\Scripts Criação Dados Sinteticos\arquivos csv\dados_sinteticos_layout_padrao_lote_chamados.csv"

with open(caminho_arquivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow([
        "MOTIVO CHAMADO", 
        "NOME", 
        "CPF", 
        "SEXO", 
        "DATA NASCIMENTO", 
        "DATA ADMISSAO", 
        "NOME DA MAE", 
        "ESTADO CIVIL", 
        "PARENTESCO", 
        "ESTUDANTE", 
        "MATRICULA EMPRESA", 
        "CNPJ CLIENTE", 
        "CARTAO SUS", 
        "EMAIL", 
        "CEP", 
        "ENDERECO", 
        "NUMERO", 
        "COMPLEMENTO", 
        "BAIRRO", 
        "CIDADE", 
        "ESTADO", 
        "SALARIO", 
        "RG", 
        "CARGO", 
        "TELEFONE", 
        "CELULAR", 
        "DATA INICIO VIGENCIA", 
        "CODIGO PLANO", 
        "FIM VIGENCIA", 
        "PRAZO ESTAGIO/J APRENDIZ (MESES)", 
        "C.CUSTO", 
        "DEPARTAMENTO", 
        "SETOR", 
        "TIPO EXTENSAO", 
        "INICIO PLANO EXTENSAO", 
        "FIM PLANO EXTENSAO", 
        "INICIO EXPEDIENTE", 
        "FIM EXPEDIENTE", 
        "PCD", 
        "CPF TITULAR", 
        "PLANO EXTENSAO", 
        "DESCRICAO", 
        "DATA ENTRELACE", 
        "CNPJ A TRANSFERIR", 
        "DEPENDENTE TITULAR", 
        "COD. OPERADORA"
    ])
    
    for _ in range(20):  # 20 linhas de dados sintéticos como exemplo
        motivo_chamado = fake.random_element(elements=["Consulta Médica", "Exame Laboratorial", "Odontologia"])
        nome = fake.name()
        cpf = fake.unique.ssn()
        sexo = fake.random_element(elements=["M", "F"])
        data_nascimento = fake.date_of_birth()
        data_admissao = fake.date_this_century(before_today=True, after_today=False)
        nome_mae = fake.first_name() + " " + fake.last_name()
        estado_civil = fake.random_element(elements=["Solteiro(a)", "Casado(a)", "Viúvo(a)"])
        parentesco = fake.random_element(elements=["Filho(a)", "Cônjuge", "Pai", "Mãe"])
        estudante = fake.random_element(elements=["Sim", "Não"])
        matricula_empresa = fake.unique.random_int(min=1000, max=9999999, step=1)
        cnpj_cliente = fake.unique.random_int(min=10000000000000, max=9999999999999999, step=1)
        cartao_sus = fake.random_element(elements=["1234567890123456", "9876543210987654"])
        email = fake.email()
        cep = fake.zipcode()
        endereco = fake.street_address()
        numero = fake.building_number()
        complemento = fake.secondary_address()
        bairro = fake.random_element(elements=["Centro", "Copacabana", "Savassi", "Moinhos de Vento"])
        cidade = fake.city()
        estado = fake.state_abbr()
        salario = random.uniform(1000, 5000)
        rg = fake.random_int(min=1000000, max=9999999999, step=1)
        cargo = fake.job()
        telefone = fake.phone_number()
        celular = fake.phone_number()
        data_inicio_vigencia = fake.date_this_century(before_today=True, after_today=False)
        codigo_plano = fake.random_int(min=1, max=10, step=1)
        fim_vigencia = fake.date_this_century(before_today=False, after_today=True)
        prazo_estagio_aprendiz = random.randint(1, 12)
        ccusto = fake.random_element(elements=["CCusto1", "CCusto2", "CCusto3"])
        departamento = fake.random_element(elements=["Recursos Humanos", "Financeiro", "Vendas"])
        setor = fake.random_element(elements=["Setor A", "Setor B", "Setor C"])
        tipo_extensao = fake.random_element(elements=["Tipo1", "Tipo2", "Tipo3"])
        inicio_plano_extensao = fake.date_this_century(before_today=True, after_today=False)
        fim_plano_extensao = fake.date_this_century(before_today=False, after_today=True)
        inicio_expediente = fake.time(pattern='%H:%M:%S', end_datetime=None)
        fim_expediente = fake.time(pattern='%H:%M:%S', end_datetime=None)
        pcd = fake.random_element(elements=["Sim", "Não"])
        cpf_titular = fake.unique.ssn()
        plano_extensao = fake.random_element(elements=["Plano A", "Plano B", "Plano C"])
        descricao = fake.sentence()
        data_entrelace = fake.date_this_century(before_today=True, after_today=False)
        cnpj_a_transferir = fake.unique.random_int(min=10000000000000, max=9999999999999999, step=1)
        dependente_titular = fake.random_element(elements=["Sim", "Não"])
        cod_operadora = fake.random_element(elements=["Operadora1", "Operadora2", "Operadora3"])

        writer.writerow([
            motivo_chamado, 
            nome, 
            cpf, 
            sexo, 
            data_nascimento, 
            data_admissao, 
            nome_mae, 
            estado_civil, 
            parentesco, 
            estudante, 
            matricula_empresa, 
            cnpj_cliente, 
            cartao_sus, 
            email, 
            cep, 
            endereco, 
            numero, 
            complemento, 
            bairro, 
            cidade, 
            estado, 
            salario, 
            rg, 
            cargo, 
            telefone, 
            celular, 
            data_inicio_vigencia, 
            codigo_plano, 
            fim_vigencia, 
            prazo_estagio_aprendiz, 
            ccusto, 
            departamento, 
            setor, 
            tipo_extensao, 
            inicio_plano_extensao, 
            fim_plano_extensao, 
            inicio_expediente, 
            fim_expediente, 
            pcd, 
            cpf_titular, 
            plano_extensao, 
            descricao, 
            data_entrelace, 
            cnpj_a_transferir, 
            dependente_titular, 
            cod_operadora
        ])

print(f"Arquivo '{caminho_arquivo_csv}' criado com sucesso com cabeçalhos nas respectivas colunas e codificação UTF-8!")
