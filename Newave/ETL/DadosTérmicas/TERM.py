import pandas as pd
import re
import os


def extract_term_data(file_path, output_excel):
    """Extrai dados do arquivo TERM.DAT, exibe como DataFrame e salva em Excel."""
    # Lista para armazenar os dados estruturados
    term_data_list = []

    # Ler o conteúdo do arquivo
    with open(file_path, "r", encoding="latin-1") as file:
        lines = file.readlines()

    # Processar cada linha do arquivo TERM.DAT, ignorando o cabeçalho
    for line in lines[2:]:  # Pular cabeçalho
        line = line.rstrip()
        num = line[:4].strip()
        nome = line[5:19].strip()
        pot = line[20:25].strip()
        fcmx = line[26:31].strip()
        teif = line[32:38].strip()
        ip = line[39:45].strip()
        gtmin = re.findall(r"\d+\.\d+", line[46:])
        gtmin = [float(x) for x in gtmin if re.match(r"^\d+\.\d+$", x)]

        if num and pot:
            term_data_list.append([
                                      int(num), nome, float(pot), float(fcmx), float(teif), float(ip)] +
                                  gtmin

                                  )
        parts = line.strip().split()
        if len(parts) >= 22:
            num = int(parts[0])
            nome = " ".join(parts[1:3]).strip()
            pot = float(parts[3])
            fcmx = float(parts[4])
            teif = float(parts[5])
            ip = float(parts[6])
            gtmin = [float(x) for x in parts[7:]]

            term_data_list.append([num, nome, pot, fcmx, teif, ip] + gtmin)

    # Criar DataFrame
    columns = ["Num", "Nome", "Potência", "FCMX", "TEIF", "IP"] + [f"Mês {i + 1}" for i in range(15)]
    df_term = pd.DataFrame(term_data_list, columns=columns)

    # Exibir DataFrame na tela
    print(df_term)

    # Salvar em um arquivo Excel
    df_term.to_excel(output_excel, index=False)
    print(f"Dados salvos em: {output_excel}")

    return df_term

# Exemplo de uso
file_path = rf"/Newave/Deck/deck_newave_2025_02_Preliminar/TERM.DAT"  # Substituir pelo caminho correto
output_excel = "usinastermicas.xlsx"
df_result = extract_term_data(file_path, output_excel)