Usando a visão para substituir o HAVING
 Próxima Atividade

Veja a consulta abaixo, que foi resposta de uma atividade anterior:

SELECT INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO, SUM(INF.QUANTIDADE) FROM ITENS_NOTAS_FISCAIS INF
INNER JOIN TABELA_DE_PRODUTOS TP 
ON INF.CODIGO_DO_PRODUTO = TP.CODIGO_DO_PRODUTO
GROUP BY INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO HAVING SUM(INF.QUANTIDADE) > 394000 
ORDER BY SUM(INF.QUANTIDADE) DESC;Copiar código
Redesenhe esta consulta, criando uma visão para a lista de quantidades totais por produto e aplicando a condição e ordenação sobre essa mesma visão.

Ver opinião do instrutor
Opinião do instrutor

Vamos criar a visão com a consulta que retorna as quantidades agregadas. Não se esqueça de criar um apelido para o agregador SUM(QUANTIDADE):

CREATE VIEW VW_QUANTIDADE_PRODUTOS AS SELECT INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO, 
SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL FROM ITENS_NOTAS_FISCAIS INF
INNER JOIN TABELA_DE_PRODUTOS TP 
ON INF.CODIGO_DO_PRODUTO = TP.CODIGO_DO_PRODUTO
GROUP BY INF.CODIGO_DO_PRODUTO, TP.NOME_DO_PRODUTO;Copiar código
Usando essa visão, selecione o que a consulta original no enunciado faz:

SELECT * FROM VW_QUANTIDADE_PRODUTOS
WHERE QUANTIDADE_TOTAL > 394000 
ORDER BY QUANTIDADE_TOTAL DESC