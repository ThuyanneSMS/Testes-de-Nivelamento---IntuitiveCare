-- 1. Top 10 operadoras com maiores despesas com SINISTROS no último trimestre

SELECT
    o.razao_social,
    o.cnpj,
    YEAR(d.data) AS ano,  -- Extrai o ano da data
    QUARTER(d.data) AS trimestre,  -- Extrai o trimestre da data
    SUM(CAST(REPLACE(d.valor_saldo_final, ',', '.') AS DECIMAL(15,2))) AS total_despesas  -- Converte valores com vírgula para ponto e faz a soma
FROM
    demonstracoes_contabeis d
JOIN
    operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE
    d.descricao LIKE '%SINISTROS%'
    AND (d.data, d.registro_ans) IN (
        SELECT
            MAX(data),
            registro_ans
        FROM demonstracoes_contabeis
        GROUP BY registro_ans
    )
GROUP BY
    o.razao_social, o.cnpj, ano, trimestre
ORDER BY
    total_despesas DESC
LIMIT 10;