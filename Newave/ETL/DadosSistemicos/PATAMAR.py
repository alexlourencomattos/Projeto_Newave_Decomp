import pandas as pd
import re


def extract_patamar_dat(file_path, output_excel):
    """
    Função para extrair dados do arquivo PATAMAR.DAT do NEWAVE, exibir como DataFrame e salvar em Excel.

    Parâmetros:
        file_path (str): Caminho do arquivo PATAMAR.DAT
        output_excel (str): Caminho do arquivo Excel de saída

    Retorna:
        DataFrame: Tabela com os dados de patamares de carga.
    """

    with open(file_path, 'r') as file:
        lines = file.readlines()

    print("Primeiras 10 linhas do arquivo:")
    print("\n".join(lines[:10]))  # Exibir primeiras 10 linhas para depuração

    data = []

    for line in lines:
        line = line.strip()
        if not line or not re.match(r'\d', line):  # Ignorar linhas vazias ou que não começam com número
            print(f"Linha ignorada (não começa com número): {line}")
            continue

        # Substituir múltiplos espaços por um único espaço para garantir separação correta
        parts = re.split(r'\s+', line)
        print(f"Partes extraídas: {parts}")  # Depuração

        if len(parts) < 4:
            print(f"Linha ignorada (formato inesperado): {line}")  # Depuração
            continue

        try:
            mes = int(parts[0])
            patamar = int(parts[1])
            percentual = float(parts[2].replace(',', '.'))  # Substituir vírgula por ponto se necessário
            carga = float(parts[3].replace(',', '.'))

            data.append([mes, patamar, percentual, carga])
        except ValueError as e:
            print(f"Erro ao processar linha: {line} - {e}")  # Depuração
            continue  # Ignorar linhas mal formatadas

    df = pd.DataFrame(data, columns=["Mês", "Patamar", "Percentual", "Carga"])

    # Exibir DataFrame na tela
    print("DataFrame final:")
    print(df)

    # Salvar em um arquivo Excel
    df.to_excel(output_excel, index=False)
    print(f"Dados salvos em: {output_excel}")

    return df


# Exemplo de uso
file_path = rf"C:\Users\alexmattos-aem\Documents\PycharmProjects\Projeto_Newave_Decomp\Newave\Deck\deck_newave_2025_02_Preliminar\PATAMAR.DAT"  # Substituir pelo caminho correto
output_excel = "Patamar.xlsx"
df_result = extract_patamar_dat(file_path, output_excel)