import pandas as pd
import re


def extract_clast_dat(file_path, output_excel):
    """
       Função para extrair dados do arquivo CLAST.DAT do NEWAVE, separando dados conjunturais e estruturais,
       exibir como DataFrame e salvar em Excel.

       Parâmetros:
           file_path (str): Caminho do arquivo CLAST.DAT
           output_excel (str): Caminho do arquivo Excel de saída

       Retorna:
           DataFrame: Tabelas com os dados conjunturais e estruturais.
       """

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    print("Primeiras 10 linhas do arquivo:")
    print("\n".join(lines[:10]))  # Exibir primeiras 10 linhas para depuração

    dados_conjunturais = []
    dados_estruturais = []
    categorias_identificadas = set()

    for line in lines:
        line = line.strip()
        if not line or not re.match(r'^\d+', line):  # Ignorar linhas vazias ou que não começam com número
            print(f"Linha ignorada (não começa com número): {line}")
            continue

        parts = re.split(r'\s+', line)
        print(f"Partes extraídas: {parts}")  # Depuração

        if len(parts) < 4:
            print(f"Linha ignorada (formato inesperado): {line}")  # Depuração
            continue

        try:
            mes = int(parts[0])
            categoria = int(parts[1])  # Categoria que diferencia conjuntural e estrutural
            percentual = float(parts[2].replace(',', '.'))  # Substituir vírgula por ponto se necessário
            carga = float(parts[3].replace(',', '.'))

            categorias_identificadas.add(categoria)

            if categoria == 1:
                dados_conjunturais.append([mes, categoria, percentual, carga])
            else:
                dados_estruturais.append([mes, categoria, percentual, carga])
        except ValueError as e:
            print(f"Erro ao processar linha: {line} - {e}")  # Depuração
            continue  # Ignorar linhas mal formatadas

    print(f"Categorias identificadas no arquivo: {categorias_identificadas}")  # Exibir categorias únicas encontradas

    df_conjuntural = pd.DataFrame(dados_conjunturais, columns=["Mês", "Categoria", "Percentual", "Carga"])
    df_estrutural = pd.DataFrame(dados_estruturais, columns=["Mês", "Categoria", "Percentual", "Carga"])

    # Exibir DataFrame na tela
    print("DataFrame Conjuntural:")
    print(df_conjuntural)
    print("DataFrame Estrutural:")
    print(df_estrutural)

    # Salvar em um arquivo Excel
    with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
        df_conjuntural.to_excel(writer, sheet_name="Conjuntural", index=False)
        df_estrutural.to_excel(writer, sheet_name="Estrutural", index=False)

    print(f"Dados salvos em: {output_excel}")

    return df_conjuntural, df_estrutural
if __name__ == "__main__":
# Exemplo de uso
    file_path = rf"C:\Users\alexmattos-aem\Documents\PycharmProjects\Projeto_Newave_Decomp\Newave\Deck\deck_newave_2025_02_Preliminar\CLAST.DAT"  # Substituir pelo caminho correto
    output_excel = "CLAST.xlsx"
    df_conjuntural, df_estrutural = extract_clast_dat(file_path, output_excel)