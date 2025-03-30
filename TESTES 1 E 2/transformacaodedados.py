import os
import pandas as pd
import pdfplumber
import zipfile

# Função para extrair e limpar dados do PDF
def extrair_dados_pdf(caminho_pdf):
    dados = []
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto = pagina.extract_text()
            if texto:
                linhas = texto.split('\n')
                for linha in linhas:
                    # Dividir a linha em colunas com base em múltiplos espaços
                    colunas = [col.strip() for col in linha.split() if col.strip()]
                    if len(colunas) > 1:  # Ignorar linhas vazias ou inválidas
                        dados.append(colunas)
    return dados

# Função para substituir abreviações pelas descrições completas
def substituir_abreviacoes(df):
    # Mapeamento das abreviações 
    mapeamento = {
        'OD': 'Odontológico',
        'AMB': 'Ambulatorial'
    }
    # Substituir valores nas colunas relevantes
    if 'Tipo' in df.columns:
        df['Tipo'] = df['Tipo'].replace(mapeamento)
    return df

# Caminho do PDF
caminho_pdf = r"C:\Users\Thuya\OneDrive\Área de Trabalho\Teste_Nivelamento\TESTE DE WEB SCRAPING\downloads\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Passo 2.1: Extrair e limpar dados do PDF
dados_extraidos = extrair_dados_pdf(caminho_pdf)

# Determinar dinamicamente o número de colunas com base nos dados extraídos
numero_colunas = max(len(linha) for linha in dados_extraidos)
colunas = ["Codigo", "Descricao", "Tipo"] + [f"Coluna_{i+4}" for i in range(numero_colunas - 3)]

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(dados_extraidos, columns=colunas)

# Remover colunas extras que podem ter sido criadas por inconsistências
df = df.iloc[:, :3]  

# Limpeza adicional: remover linhas com valores nulos ou inconsistentes
df.dropna(subset=["Codigo", "Descricao"], inplace=True)

# Substituir abreviações pelas descrições completas
df = substituir_abreviacoes(df)

# Salvar o DataFrame em um arquivo CSV
nome_arquivo_csv = "Rol_de_Procedimentos.csv"
df.to_csv(nome_arquivo_csv, index=False, encoding='utf-8')

# Passo 2.3: Compactar o CSV em um arquivo ZIP
nome_arquivo_zip = "Teste_Thuy.zip" 
with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
    zipf.write(nome_arquivo_csv, arcname=os.path.basename(nome_arquivo_csv))

print(f"Arquivo CSV salvo como '{nome_arquivo_csv}' e compactado em '{nome_arquivo_zip}'.")