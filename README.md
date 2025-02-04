# Projeto: Extração e Manipulação de Dados do Newave e Decomp

Este projeto é uma ferramenta para a extração, exibição, edição e reescrita de dados contidos no arquivo **EXPT.DAT**, usado no contexto de planejamento energético.

## Funcionalidades

- **Leitura e Processamento**: Extrai os dados do arquivo `EXPT.DAT` e organiza-os em um formato tabular usando pandas.
- **Visualização Interativa**: Permite visualizar os dados em uma interface interativa através do Streamlit.
- **Edição e Atualização**: Após editar os dados, as alterações podem ser salvas diretamente no arquivo `EXPT.DAT`.
- **Exportação para Excel**: Salva os dados extraídos em um arquivo Excel para uso externo.

## Requisitos

Certifique-se de que os seguintes requisitos estão instalados no seu ambiente:

- Python 3.8+
- Bibliotecas Python:
  - `pandas`
  - `streamlit`
  - `re`

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/Projeto_Newave_Decomp.git
   cd Projeto_Newave_Decomp
   ```

2. Instale os requisitos:
   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que o arquivo `EXPT.DAT` está no diretório correto.

4. Execute o script com o Streamlit:
   ```bash
   streamlit run extract_expt_data.py
   ```

5. No navegador, visualize e edite os dados exibidos.

6. Após a edição, os dados serão salvos automaticamente no arquivo `EXPT.DAT` e exportados para `expansao_termica.xlsx`.

## Estrutura do Código

O script principal é `extract_expt_data.py`, que realiza as seguintes etapas:

1. **Leitura do Arquivo**:
   - Lê o arquivo `EXPT.DAT` linha por linha.
   - Utiliza expressões regulares para identificar e extrair os campos.

2. **Processamento dos Dados**:
   - Organiza os dados em um `DataFrame` com colunas específicas (e.g., `Num`, `Tipo`, `Modificação`, etc.).

3. **Visualização**:
   - Usa o Streamlit para exibir os dados de forma interativa.

4. **Edição e Atualização**:
   - Salva as alterações diretamente no arquivo `EXPT.DAT`.
   - Exporta os dados para um arquivo Excel (`expansao_termica.xlsx`).

## Formato do Arquivo EXPT.DAT

O arquivo `EXPT.DAT` deve ter o seguinte formato:
```
NUM   TIPO   MODIF  MI ANOI MF ANOF   NOME_USINA
1     POTEF  100.00 1 2025 12 2025   USINA_A
2     FCMAX  200.00 2 2026           USINA_B
```

Cada campo possui largura fixa:
- `NUM`: Número da usina (inteiro)
- `TIPO`: Tipo de modificação (e.g., POTEF, FCMAX)
- `MODIF`: Valor da modificação (float)
- `MI/ANOI`: Mês e Ano de início
- `MF/ANOF`: Mês e Ano de fim (opcional)
- `NOME_USINA`: Nome da usina

