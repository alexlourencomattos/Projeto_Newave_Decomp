import pandas as pd
import re
import os


def extract_sistema_data(file_path, output_excel):
    """Extrai dados do arquivo SISTEMA.DAT, exibe como DataFrame e salva em Excel."""
    # Lista para armazenar os dados estruturados
    sistema_data_list = []

    # Ler o conteúdo do arquivo
    with open(file_path, "r", encoding="latin-1") as file:
        lines = file.readlines()

    # Processar cada linha do arquivo SISTEMA.DAT, ignorando cabeçalhos
    for line in lines[7:]:  # Pular cabeçalhos
        if not line[0].isdigit():  # Ignorar linhas que não começam com um número
            continue
        parts = line.strip().split()
        if len(parts) >= 12:
            num = int(parts[0])
            nome = " ".join(parts[1:3]).strip()
            custo_deficit = [float(x) for x in parts[3:7]]
            pu_corte = [float(x) for x in parts[7:]]

            sistema_data_list.append([num, nome] + custo_deficit + pu_corte)

    # Criar DataFrame
    columns = ["Num", "Subsistema", "Custo Patamar 1", "Custo Patamar 2", "Custo Patamar 3", "Custo Patamar 4",
               "PU Corte 1", "PU Corte 2", "PU Corte 3", "PU Corte 4", "Extra 1", "Extra 2"]
    df_sistema = pd.DataFrame(sistema_data_list, columns=columns)

    # Exibir DataFrame na tela
    print(df_sistema)

    # Salvar em um arquivo Excel
    df_sistema.to_excel(output_excel, index=False)
    print(f"Dados salvos em: {output_excel}")

    return df_sistema



# Exemplo de uso
file_path = rf"/Newave/Deck/deck_newave_2025_02_Preliminar/SISTEMA.DAT"  # Substituir pelo caminho correto
output_excel = "sistema_deficit.xlsx"
df_result = extract_sistema_data(file_path, output_excel)