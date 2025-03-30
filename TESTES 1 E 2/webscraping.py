import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile

# URL do site
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Diretório para salvar os arquivos baixados
download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

# Função para baixar arquivos
def download_file(file_url, save_path):
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Arquivo baixado: {save_path}")
    else:
        print(f"Falha ao baixar o arquivo: {file_url}")

# Acessar o site e buscar os links dos anexos
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Procurar links que contêm "Anexo I" e "Anexo II"
    anexos_links = []
    for link in soup.find_all('a', href=True):
        text = link.get_text(strip=True).lower()
        if "anexo i" in text or "anexo ii" in text:
            file_url = urljoin(url, link['href'])
            anexos_links.append(file_url)
    
    # Baixar os arquivos encontrados
    downloaded_files = []
    for file_url in anexos_links:
        file_name = os.path.join(download_dir, file_url.split('/')[-1])
        download_file(file_url, file_name)
        downloaded_files.append(file_name)
else:
    print("Falha ao acessar o site.")
    exit()

# Compactar os arquivos baixados em um único arquivo ZIP
if downloaded_files:
    zip_filename = "anexos.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in downloaded_files:
            zipf.write(file, os.path.basename(file))
            print(f"Arquivo adicionado ao ZIP: {file}")
    print(f"Arquivos compactados em: {zip_filename}")
else:
    print("Nenhum arquivo foi baixado para compactar.")

print("Processo concluído.")