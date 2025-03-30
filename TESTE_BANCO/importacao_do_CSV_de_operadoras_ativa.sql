LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/operadoras.csv' -- Ajuste o caminho conforme seu sistema
INTO TABLE operadoras_ativas
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;