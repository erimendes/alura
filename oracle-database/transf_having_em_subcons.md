Transformando o HAVING em subconsultas
 Próxima Atividade

Veja a consulta abaixo, que foi resposta de uma atividade anterior:

SELECT INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO, SUM(INF.QUANTIDADE) FROM ITENS_NOTAS_FISCAIS INF
INNER JOIN TABELA_DE_PRODUTOS TP 
ON INF.CODIGO_DO_PRODUTO = TP.CODIGO_DO_PRODUTO
GROUP BY INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO HAVING SUM(INF.QUANTIDADE) > 394000 
ORDER BY SUM(INF.QUANTIDADE) DESC;Copiar código
Redesenhe esta consulta usando subconsultas.

Ver opinião do instrutor
Opinião do instrutor

Vamos separar a consulta que nos dá o valor das quantidades agrupadas:

SELECT INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO, SUM(INF.QUANTIDADE) FROM ITENS_NOTAS_FISCAIS INF
INNER JOIN TABELA_DE_PRODUTOS TP 
ON INF.CODIGO_DO_PRODUTO = TP.CODIGO_DO_PRODUTO
GROUP BY INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO;Copiar código
Agora construímos uma consulta usando esta outra no seu FROM.

Não esqueça de incluir um apelido para SUM(QUANTIDADE) e outro para a consulta que ficará dentro do FROM:

SELECT SC.CODIGO_DO_PRODUTO, SC.NOME_DO_PRODUTO, SC.QUANTIDADE_TOTAL
FROM
(SELECT INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO, SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL FROM ITENS_NOTAS_FISCAIS INF
INNER JOIN TABELA_DE_PRODUTOS TP 
ON INF.CODIGO_DO_PRODUTO = TP.CODIGO_DO_PRODUTO
GROUP BY INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO) SC;Copiar código
Finalmente aplicamos a ordenação e o filtro:

SELECT SC.CODIGO_DO_PRODUTO, SC.NOME_DO_PRODUTO, SC.QUANTIDADE_TOTAL
FROM
(SELECT INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO, SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL FROM ITENS_NOTAS_FISCAIS INF
INNER JOIN TABELA_DE_PRODUTOS TP 
ON INF.CODIGO_DO_PRODUTO = TP.CODIGO_DO_PRODUTO
GROUP BY INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO) SC
WHERE SC.QUANTIDADE_TOTAL > 394000 
ORDER BY SC.QUANTIDADE_TOTAL DESC