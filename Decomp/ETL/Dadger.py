import pandas as pd

def extrair_bloco_ct(file_path):
    """
    Função para extrair o bloco CT de um arquivo DADGER.
    """
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    # Encontrar as linhas do bloco CT
    bloco_ct = []
    dentro_bloco_ct = False

    for line in lines:
        if line.startswith("CT"):  # Identifica o início do bloco CT
            dentro_bloco_ct = True
            bloco_ct.append(line)
        elif dentro_bloco_ct and not line.startswith("CT"):  # Sai do bloco quando encontra outra seção
            break

    return bloco_ct

# Extrair o bloco CT dos arquivos DADGER
bloco_ct_sem1 = extrair_bloco_ct(r"C:\Users\alexmattos-aem\Documents\PycharmProjects\Projeto_Newave_Decomp\Decomp\Deck\DC202502-sem1.zip/dadger.rv0")
bloco_ct_sem2 = extrair_bloco_ct("/mnt/data/DC202502-sem2/dadger.rv1")

# Juntar os resultados
bloco_ct_completo = bloco_ct_sem1

# Criar DataFrame a partir do bloco CT
colunas = ["CT", "REE", "SEM", "USINA", "TIPO", "COEF1", "COEF2", "COEF3", "CORTE"]
dados_ct = []

for linha in bloco_ct_completo:
    partes = linha.split()
    if len(partes) >= 8:  # Garantir que há dados suficientes na linha
        dados_ct.append([
            partes[0],  # CT
            partes[1],  # REE
            partes[2],  # SEM
            " ".join(partes[3:-5]),  # Nome da usina (pode ter espaços)
            partes[-5],  # Tipo
            partes[-4],  # Coeficiente 1
            partes[-3],  # Coeficiente 2
            partes[-2],  # Coeficiente 3
            partes[-1]   # Corte
        ])

df_ct = pd.DataFrame(dados_ct, columns=colunas)

# Salvar em arquivo Excel
output_path = "/mnt/data/bloco_CT_DADGER.xlsx"
df_ct.to_excel(output_path, index=False)

print(f"Bloco CT extraído e salvo em: {output_path}")
