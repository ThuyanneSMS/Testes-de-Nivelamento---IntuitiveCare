# Teste Técnico de Nivelamento IntuitiveCare

Desenvolvi os testes abaixo para atender às tarefas solicitadas. Este documento descreve os objetivos de cada teste e as tecnologias que utilizei.

---

## 1. TESTE DE WEB SCRAPING

### Objetivo
O objetivo foi criar um script para acessar um site específico, baixar os arquivos PDF dos Anexos I e II fornecidos e compactá-los em um único arquivo.

### Tecnologias Utilizadas
- Python: `requests`, `BeautifulSoup`, `zipfile`.  
---

## 2. TESTE DE TRANSFORMAÇÃO DE DADOS

### Objetivo
Busquei extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do Anexo I, salvá-los em um CSV estruturado, compactar o arquivo e substituir abreviações por descrições completas.

### Tecnologias Utilizadas
- Python: `PyPDF2`, `pdfplumber`, `pandas`, `zipfile`.
  
---

## 3. TESTE DE BANCO DE DADOS

### Objetivo
Criação de scripts SQL para estruturar tabelas, importar dados de operadoras de saúde e desenvolver uma query analítica para identificar as 10 operadoras com maiores despesas em eventos/sinistros no último trimestre e ano.

### Tecnologias Utilizadas
- MySQL 8.0+ .

---

## 4. TESTE DE API

### Objetivo
Desenvolvi uma interface web integrada a um servidor para realizar busca textual em dados de operadoras, retornando os registros mais relevantes, e documentei o resultado em uma coleção no Postman.

### Tecnologias Utilizadas
- Backend: Python com `Flask`
- Frontend: Vue.js.  
- Testes: Postman.

---
