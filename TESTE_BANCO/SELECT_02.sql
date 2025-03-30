-- 2. Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

SELECT
    o.razao_social,
    o.cnpj,
    SUM(CAST(REPLACE(d.valor_saldo_final, ',', '.') AS DECIMAL(15,2))) AS total_despesas
FROM
    demonstracoes_contabeis d
JOIN
    operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE
    d.descricao LIKE '%SINISTROS%'  -- Troca de ILIKE para LIKE no MySQL
    AND YEAR(d.data) = (
        SELECT MAX(YEAR(data)) FROM demonstracoes_contabeis
    )
GROUP BY
    o.razao_social, o.cnpj
ORDER BY
    total_despesas DESC
LIMIT 10;