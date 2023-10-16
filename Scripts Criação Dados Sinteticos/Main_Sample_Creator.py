import subprocess

scripts_a_executar = ["Sample_Sintetic_Data_base_medica_utilização.py"
                      , "Sample_Sintetic_Data_Cadastro_de_Associados.py"
                      , "Sample_Sintetic_Data_layout_atestados.py"
                      , "Sample_Sintetic_Data_layout_padrao_lote_chamados.py"
                      , "Sample_Sintetic_Data_relatorio_cuidando_de_voce.py"]

for script in scripts_a_executar:
    try:
        subprocess.run(["python", script], check=True)
        print(f"Script {script} executado com sucesso.")
    except subprocess.CalledProcessError:
        print(f"Erro ao executar o script {script}.")

if __name__ == "__main__":
    print("Executando os scripts...")