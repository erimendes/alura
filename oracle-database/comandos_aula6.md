Chegou a hora de você pôr em prática o que foi visto na aula. Para isso, execute os passos listados abaixo.

1) Crie um novo script e olhe a tabela de cadastro de clientes:

SELECT * FROM TABELA_DE_CLIENTES;Copiar código
2) Para calcular a quantidade vendida por cliente, execute o código:

SELECT
NF.CPF,
NF.DATA_VENDA,
INF.QUANTIDADE
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO;Copiar código
3) Para agregar dentro de um mesmo mês, execute:

SELECT
NF.CPF,
TO_CHAR(NF.DATA_VENDA,'MM-YYYY') AS MES_ANO,
INF.QUANTIDADE
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO;Copiar código
4) Agrupe:

SELECT
NF.CPF,
TO_CHAR(NF.DATA_VENDA,'MM-YYYY') AS MES_ANO,
SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO
GROUP BY
CPF, TO_CHAR(NF.DATA_VENDA,'MM-YYYY');Copiar código
5) Olhe a tabela de clientes:

SELECT CPF, NOME, VOLUME_DE_COMPRA FROM TABELA_DE_CLIENTES;Copiar código
6) Junte o resultado da query da tabela de clientes com o resultado da consulta anterior, mostrando o cadastro e a quantidade total:

SELECT
TC.CPF, TC.NOME, TC.VOLUME_DE_COMPRA, TV.MES_ANO, TV.QUANTIDADE_TOTAL
FROM
TABELA_DE_CLIENTES TC
INNER JOIN
(
SELECT
NF.CPF,
TO_CHAR(NF.DATA_VENDA,'MM-YYYY') AS MES_ANO,
SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO
GROUP BY
CPF, TO_CHAR(NF.DATA_VENDA,'MM-YYYY')
) TV
ON TV.CPF = TC.CPF;Copiar código
7) Coloque o CASE para testar se as vendas são válidas:

SELECT
TC.CPF, TC.NOME, TC.VOLUME_DE_COMPRA, TV.MES_ANO, TV.QUANTIDADE_TOTAL,
(CASE WHEN TC.VOLUME_DE_COMPRA >= TV.QUANTIDADE_TOTAL THEN 'VENDAS VÁLIDAS'
ELSE 'VENDAS INVÁLIDAS' END) AS RESULTADO
FROM
TABELA_DE_CLIENTES TC
INNER JOIN
(SELECT
NF.CPF,
TO_CHAR(NF.DATA_VENDA,'MM-YYYY') AS MES_ANO,
SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO
GROUP BY
CPF, TO_CHAR(NF.DATA_VENDA,'MM-YYYY')) TV
ON TV.CPF = TC.CPF;Copiar código
8) Agora, escolha a data que quer verificar:

SELECT
TC.CPF, TC.NOME, TC.VOLUME_DE_COMPRA, TV.MES_ANO, TV.QUANTIDADE_TOTAL,
(CASE WHEN TC.VOLUME_DE_COMPRA >= TV.QUANTIDADE_TOTAL THEN 'VENDAS VÁLIDAS'
ELSE 'VENDAS INVÁLIDAS' END) AS RESULTADO
FROM
TABELA_DE_CLIENTES TC
INNER JOIN
(SELECT
NF.CPF,
TO_CHAR(NF.DATA_VENDA,'MM-YYYY') AS MES_ANO,
SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO
GROUP BY
CPF, TO_CHAR(NF.DATA_VENDA,'MM-YYYY')) TV
ON TV.CPF = TC.CPF
WHERE TV.MES_ANO = '02-2015';Copiar código
9) O novo desafio é o ranking das vendas dos produtos por sabor e uma coluna do percentual de vendas no ano.

10) Crie um novo script e desenvolva o código para pegar as vendas totais por sabor:

SELECT
TP.SABOR
,INF.QUANTIDADE
,NF.DATA_VENDA
FROM
TABELA_DE_PRODUTOS TP
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON TP.CODIGO_DO_PRODUTO = INF.CODIGO_DO_PRODUTO
INNER JOIN
NOTAS_FISCAIS NF
ON INF.NUMERO = NF.NUMERO;Copiar código
11) Melhore o código, para mostrar dentro do ano:

SELECT
TP.SABOR
,INF.QUANTIDADE
,EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO
FROM
TABELA_DE_PRODUTOS TP
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON TP.CODIGO_DO_PRODUTO = INF.CODIGO_DO_PRODUTO
INNER JOIN
NOTAS_FISCAIS NF
ON INF.NUMERO = NF.NUMERO;Copiar código
12) De maneira a mostrar o ranking de vendas no ano 2016, ordenando pela soma das quantidades, execute:

SELECT
TP.SABOR
,EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO
,SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
FROM
TABELA_DE_PRODUTOS TP
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON TP.CODIGO_DO_PRODUTO = INF.CODIGO_DO_PRODUTO
INNER JOIN
NOTAS_FISCAIS NF
ON INF.NUMERO = NF.NUMERO
WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
GROUP BY 
TP.SABOR
,EXTRACT(YEAR FROM NF.DATA_VENDA)
ORDER BY SUM(INF.QUANTIDADE) DESC;Copiar código
13) Para mostrar a consulta da data e quantidade de vendas:

SELECT
NF.DATA_VENDA
,INF.QUANTIDADE
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO;Copiar código
14) Altere o código para mostrar o total de vendas em litros:

SELECT TOTAL_ANO.QUANTIDADE_GERAL FROM
(SELECT
EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO
,SUM(INF.QUANTIDADE) AS QUANTIDADE_GERAL
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO
WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
GROUP BY EXTRACT(YEAR FROM NF.DATA_VENDA)) TOTAL_ANO;Copiar código
15) Juntando as consultas, você terá:

SELECT
TP.SABOR
,EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO
,SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
,(SELECT TOTAL_ANO.QUANTIDADE_GERAL FROM
(SELECT
EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO
,SUM(INF.QUANTIDADE) AS QUANTIDADE_GERAL
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO
WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
GROUP BY EXTRACT(YEAR FROM NF.DATA_VENDA)) TOTAL_ANO
) AS QUANTIDADE_GERAL
FROM
TABELA_DE_PRODUTOS TP
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON TP.CODIGO_DO_PRODUTO = INF.CODIGO_DO_PRODUTO
INNER JOIN
NOTAS_FISCAIS NF
ON INF.NUMERO = NF.NUMERO
WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
GROUP BY 
TP.SABOR
,EXTRACT(YEAR FROM NF.DATA_VENDA)
ORDER BY SUM(INF.QUANTIDADE) DESC;Copiar código
16) Para finalizar, o código completo que calcula e mostra a quantidade de vendas por sabor em determinado ano:

SELECT CONSULTA_RELATORIO.SABOR, 
CONSULTA_RELATORIO.ANO,
CONSULTA_RELATORIO.QUANTIDADE_TOTAL,
ROUND((CONSULTA_RELATORIO.QUANTIDADE_TOTAL/CONSULTA_RELATORIO.QUANTIDADE_GERAL)*100,2) AS 
PERCENTUAL_PARTICIPACAO
FROM
(SELECT
TP.SABOR,EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO ,SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
,(SELECT TOTAL_ANO.QUANTIDADE_GERAL FROM
(SELECT
EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO
,SUM(INF.QUANTIDADE) AS QUANTIDADE_GERAL
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO
WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
GROUP BY EXTRACT(YEAR FROM NF.DATA_VENDA)) TOTAL_ANO
) AS QUANTIDADE_GERAL
FROM TABELA_DE_PRODUTOS TP
INNER JOIN ITENS_NOTAS_FISCAIS INF
ON TP.CODIGO_DO_PRODUTO = INF.CODIGO_DO_PRODUTO
INNER JOIN NOTAS_FISCAIS NF
ON INF.NUMERO = NF.NUMERO
WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
GROUP BY TP.SABOR,EXTRACT(YEAR FROM NF.DATA_VENDA)
ORDER BY SUM(INF.QUANTIDADE) DESC) CONSULTA_RELATORIO;

Transcrição
No último vídeo, fizemos uma query cujo resultado ficou bem grande. Nós vamos copiá-la para um novo script vazio.

SELECT CONSULTA_RELATORIO.SABOR,
CONSULTA_RELATORIO.ANO,
CONSULTA_RELATORIO.QUANTIDADE_TOTAL,
ROUND((CONSULTA_RELATORIO.QUANTIDADE_TOTAL/CONSULTA_RELATORIO.QUANTIDADE_GERAL)*100,2) AS
PERCENTUAL_PARTICIPACAO
FROM
(SELECT
TP.SABOR,EXTRACT(YEAR FROM NF.DATA_VENDA AS ANO ,SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
,(SELECT TOTAL_ANO.QUANTIDADE_GERAL FROM
(SELECT
EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO
,SUM(INF.QUANTIDADE) AS QUANTIDADE_GERAL
FROM
NOTAS_FISCAIS NF
INNER JOIN
ITENS_NOTAS_FISCAIS INF
ON NF.NUMERO = INF.NUMERO
WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
GROUP BY EXTRACT(YEAR FROM NF.DATA_VENDA)) TOTAL_ANO
) AS QUANTIDADE_GERAL
FROM TABELA_DE_PRODUTOS TP
INNER JOIN ITENS_NOTAS_FISCAIS INF
ON TP.CODIGO_DO_PRODUTO = INF.CODIGO_DO_PRODUTO
INNER JOIN NOTAS_FISCAIS NF
ON INF.NUMERO = NF.NUMERO
WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
GROUP BY TP.SABOR,EXTRACT(YEAR FROM NF.DATA_VENDA)
ORDER BY SUM(INF.QUANTIDADE) DESC) CONSULTA_RELATORIO;Copiar código
Ao rodar a query pela primeira vez, faltava o comando FROM na sexta linha de código e houve um erro, que depois descobrimos ser a ausência do comando.

Quando temos um erro muito grande, pode ser difícil conseguir achá-lo na consulta. Por isso, é interessante formatar consultas SQL muito extensas em um padrão que te faça encontrar melhor os erros.

Às vezes, esquecemos de acrescentar vírgulas ao final de linhas de código, por exemplo, o que gera erro ao rodar. Em consultas grandes demais, pode ser difícil encontrar o problema.

Exemplo:

-- código omitido

CONSULTA_RELATORIO.ANO

-- código omitidoCopiar código
Sendo assim, um padrão que eu costumo utilizar é sempre colocar as vírgulas no início da linha de código. Assim, torna-se mais fácil encontrar os resultados e cada linha tem uma sentença completa.

SELECT 
CONSULTA_RELATORIO.SABOR
, CONSULTA_RELATORIO.ANO
, CONSULTA_RELATORIO.QUANTIDADE_TOTAL
, ROUND((CONSULTA_RELATORIO.QUANTIDADE_TOTAL/CONSULTA_RELATORIO.QUANTIDADE_GERAL)*100,2) AS PERCENTUAL_PARTICIPACAO

-- código omitidoCopiar código
A partir de FROM, teclaremos "Tab" para começar novas queries e "Enter" para organizar os dados no código. A cada query iniciada, jogamos o código para a direita.

-- código omitido

FROM
    (SELECT
        TP.SABOR,EXTRACT(YEAR FROM NF.DATA_VENDA AS ANO 
        ,SUM(INF.QUANTIDADE) AS QUANTIDADE_TOTAL
        ,
            (SELECT TOTAL_ANO.QUANTIDADE_GERAL FROM
                (SELECT
                    EXTRACT(YEAR FROM NF.DATA_VENDA) AS ANO
                    ,SUM(INF.QUANTIDADE) AS QUANTIDADE_GERAL
                    FROM
                    NOTAS_FISCAIS NF INNER JOIN ITENS_NOTAS_FISCAIS INF ON NF.NUMERO = INF.NUMERO
                    WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
                    GROUP BY EXTRACT(YEAR FROM NF.DATA_VENDA)) TOTAL_ANO
                ) AS QUANTIDADE_GERAL
                FROM TABELA_DE_PRODUTOS TP
                INNER JOIN ITENS_NOTAS_FISCAIS INF ON TP.CODIGO_DO_PRODUTO = INF.CODIGO_DO_PRODUTO
                INNER JOIN NOTAS_FISCAIS NF
ON INF.NUMERO = NF.NUMERO
                WHERE EXTRACT(YEAR FROM NF.DATA_VENDA) = 2016
                GROUP BY TP.SABOR,EXTRACT(YEAR FROM NF.DATA_VENDA)
            ORDER BY SUM(INF.QUANTIDADE) DESC) 
            CONSULTA_RELATORIO;Copiar código
Costumamos colocar os INNER JOIN inseridos na linha de código, conforme visto no bloco de código acima.

Na linha de código 14, fechamos o parêntese da query da linha 7. As linhas de código abaixo fazem parte dessa mesma consulta. Finalizados todos os ajustes, fechamos a consulta final.

Feito isso, ao rodá-la, teremos como resultado a mesma tabela do vídeo anterior, porém a consulta está melhor organizada.

Utilize o critério que achar melhor para formatar a sua consulta. No entanto, caso esteja usando o SQL Developer, você pode selecionar a sua consulta e clicar sobre ela com o botão direito do mouse para acessar a opção “Formatar” (atalho: "Ctrl + F7"). Com isso, o SQL formata a sua consulta no formato interno da ferramenta.

Vamos clicar nessa opção para ver o resultado?
SELECT 
    consulta_relatorio.sabor,
    consulta_relatorio.ano,
    consulta_relatorio.quantidade_total,
    round((consulta_relatorio.quantidade_total / consulta_relatorio.quantidade_geral) * 100, 2) AS percentual_participacao
FROM
    (
        SELECT
            tp.sabor,
            EXTRACT(YEAR FROM nf.data_venda) AS ano, 
            SUM(inf.quantidade)              AS quantidade_total,
            (
                SELECT 
                    total_ano.quantidade_geral 
                FROM
                    (
                        SELECT
                            EXTRACT(YEAR FROM nf.data_venda) AS ano,
                            SUM(inf.quantidade)              AS quantidade_geral
                        FROM
                                notas_fiscais nf 
                            INNER JOIN itens_notas_fiscais inf ON nf.numero = inf.numero
                        WHERE
                            EXTRACT(YEAR FROM nf.data_venda) = 2016
                        GROUP BY 
                            EXTRACT(YEAR FROM nf.data_venda)
                    ) total_ano
            )                                AS quantidade_geral
        FROM
                tabela_de_produtos tp
            INNER JOIN itens_notas_fiscais inf ON tp.codigo_do_produto = inf.codigo_do_produto
                INNER JOIN notas_fiscais   nf ON inf.numero = nf.numero
        WHERE
            EXTRACT(YEAR FROM nf.data_venda) = 2016
        GROUP BY 
            tp.sabor,
            EXTRACT(YEAR FROM nf.data_venda)
            ORDER BY
                SUM(inf.quantidade) DESC
    ) consulta_relatorio;Copiar código
Perceba que a ferramenta colocou os campos em minúsculo, pois eles estão definidos dessa forma na estrutura do banco de dados. Dessa forma, conseguimos enxergar melhor o resultado.

Caso queira, você pode pesquisar por “SQL Formatter” na internet, por exemplo. Você encontrará vários softwares que podem ser utilizados para formatar consultas.

Vou copiar a minha consulta e colar em um deles (Instant SQL Formatter). Nesse site, podemos escolher a sintaxe; no meu caso, vou selecionar “Oracle/PLSQL” e clicar no botão “Format SQL”. Feito isso, temos a consulta formatada.

SELECT consulta_relatorio.sabor,
       consulta_relatorio.ano,
       consulta_relatorio.quantidade_total,
       Round(( consulta_relatorio.quantidade_total /
               consulta_relatorio.quantidade_geral ) *
            100, 2) AS percentual_participacao
FROM   (SELECT tp.sabor,
               Extract(year FROM nf.data_venda)
               AS ano, 
               SUM(inf.quantidade)
               AS
                      quantidade_total,
               (SELECT total_ano.quantidade_geral 
                FROM   (SELECT Extract(year FROM nf.data_venda) AS ano,
                               SUM(inf.quantidade)              AS
                               quantidade_geral
                        FROM   notas_fiscais nf 
                               inner join itens_notas_fiscais inf 
                                       ON nf.numero = inf.numero
                        WHERE Extract(year FROM nf.data_venda) = 2016
                        GROUP BY Extract(year FROM nf.data_venda)) total_ano)
               AS
               quantidade_geral
        FROM   tabela_de_produtos tp
               inner join itens_notas_fiscais inf 
                       ON tp.codigo_do_produto = inf.codigo_do_produto
               inner join notas_fiscais nf 
                       ON inf.numero = nf.numero
        WHERE  Extract(year FROM nf.data_venda) = 2016
        GROUP BY tp.sabor,
                 Extract(year FROM nf.data_venda)
        ORDER BY SUM(inf.quantidade) DESC) consulta_relatorio;Copiar código
O resultado da formatação é um bloco de código bastante colorido, em que conseguimos identificar bem o que é cada elemento: palavras reservadas estão em azul; funções, em vermelho; e campos e INNER JOIN têm uma cor mais neutra.

Uma vez formatada, podemos copiá-la e colar no SQL Developer; ao rodar, você terá o mesmo resultado.

Conclusão
Nesse vídeo, quis mostrar a importância de formatar e apresentar bem o seu SQL, não somente para fazer uma boa documentação, mas também para que você consiga encontrar eventuais erros.

