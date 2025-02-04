import pandas as pd
import re
import os

import tools


def extract_expt_data(file_path, output_excel):
    """Extrai dados do arquivo EXPT.DAT, exibe como DataFrame e salva em Excel."""
    # Lista para armazenar os dados estruturados
    expansion_data = []

    # Regex para identificar os padrões das colunas
    pattern = re.compile(r"(\d+)\s+(\w+)\s+([\d\.\-]+)\s+(\d+)\s+(\d+)\s*(\d*)\s*(\d*)\s*(.*)")

    # Ler o conteúdo do arquivo
    with open(file_path, "r", encoding="latin-1") as file:
        lines = file.readlines()

    # Processar cada linha do arquivo EXPT.DAT
    for line in lines[2:]:  # Pular cabeçalho
        match = pattern.match(line.strip())
        if match:
            num, tipo, modif, mi, anoi, mf, anof, nome = match.groups()
            expansion_data.append([
                int(num), tipo, float(modif), int(mi), int(anoi),
                int(mf) if mf else None, int(anof) if anof else None, nome.strip()
            ])

    # Criar DataFrame
    columns = ["Num", "Tipo", "Modificação", "Mês Início", "Ano Início", "Mês Fim", "Ano Fim", "Nome Usina"]
    df_expt = pd.DataFrame(expansion_data, columns=columns)

    import streamlit as st
    st.dataframe(df_expt)

    # Salvar em um arquivo Excel
    df_expt.to_excel(output_excel, index=False)

    # Salvar alterações de volta no arquivo EXPT.DAT
    with open(file_path, "w", encoding="latin-1") as file:
     file.write("NUM   TIPO   MODIF  MI ANOI MF ANOF")  # Escrever cabeçalho original
    for _, row in df_expt.iterrows():
        file.write(f"{row['Num']:4} {row['Tipo']:6} {row['Modificação']:8.2f} {row['Mês Início']:2} {row['Ano Início']:4} "f"{row['Mês Fim'] if row['Mês Fim'] else '':2} {row['Ano Fim'] if row['Ano Fim'] else '':4} {row['Nome Usina']}")
    return df_expt


# Exemplo de uso
file_path = rf"C:\Users\alexmattos-aem\Documents\PycharmProjects\Projeto_Newave_Decomp\Newave\Deck\deck_newave_2025_02_Preliminar\EXPT.DAT"  # Substituir pelo caminho correto
output_excel = "expansao_termica.xlsx"
df_result = extract_expt_data(file_path, output_excel)

