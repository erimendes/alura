Chegou a hora de você pôr em prática o que foi visto na aula. Para isso, execute os passos listados abaixo.

1) No Oracle SQL Developer, abra uma nova janela de script.

2) Clique no ícone da esquerda Novo, escolha a opção Arquivo de Banco de Dados e nomeie como 2580-video2.1.

3) Digite com o comando abaixo para mostrar todos os campos da tabela TABELA_DE_CLIENTES:

SELECT * FROM TABELA_DE_CLIENTES;Copiar código
4) Clique no ícone Executar.

5) Execute o comando abaixo para mostrar somente os quatro campos.

SELECT CPF, NOME, BAIRRO, CIDADE FROM TABELA_DE_CLIENTES;Copiar código
6) Trocando a ordem de visualização dos campos, execute o código:

SELECT NOME, CPF, CIDADE, BAIRRO FROM TABELA_DE_CLIENTES;Copiar código
7) Use alias para alterar o nome do campo ao ser mostrado. Execute o código:

SELECT CPF AS IDENTIFICADOR, NOME AS "NOME DE CLIENTE", BAIRRO, CIDADE FROM TABELA_DE_CLIENTES;Copiar código
8) Para dar um Alias para a tabela, execute o comando:

SELECT CPF AS IDENTIFICADOR, NOME AS "NOME DE CLIENTE", TDC.BAIRRO, CIDADE FROM TABELA_DE_CLIENTES TDC;Copiar código
9) Associe uma tabela para um Alias:

SELECT TDC.* FROM TABELA_DE_CLIENTES TDC;Copiar código
10) Clique no ícone da esquerda Novo, escolha a opção Arquivo de Banco de Dados e nomeie o script como 2580-video2.2.

11) Para ver todas as linhas da tabela, execute o comando:

SELECT * FROM TABELA_DE_PRODUTOS;Copiar código
12) Execute o comando com o filtro WHERE 1=1:

SELECT * FROM TABELA_DE_PRODUTOS WHERE 1=1;Copiar código
13) Para mostrar a linha com o determinado código, execute o comando:

SELECT * FROM TABELA_DE_PRODUTOS WHERE CODIGO_DO_PRODUTO = '290478';Copiar código
14) Para mostrar um conjunto de campos, execute:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR = 'Laranja';Copiar código
15) Use o filtro no campo EMBALAGEM:

SELECT * FROM TABELA_DE_PRODUTOS WHERE EMBALAGEM = 'PET';Copiar código
16) O comando é case sensitive, então não funcionará:

SELECT * FROM TABELA_DE_PRODUTOS WHERE EMBALAGEM = 'pet';Copiar código
17) Para exercitar os filtros quantitativos, crie um novo script, chamado 2580-video2.3.

18) Execute o comando:

SELECT * FROM TABELA_DE_CLIENTES;Copiar código
19) Para usar o filtro quantitativo, mostre clientes com mais de 20 anos:

SELECT * FROM TABELA_DE_CLIENTES WHERE IDADE > 20;Copiar código
20) Execute o comando abaixo para mostrar os clientes com menos de 20 anos:

SELECT * FROM TABELA_DE_CLIENTES WHERE IDADE < 20;Copiar código
21) Para mostrar os clientes que não tem 18 anos, execute o comando:

SELECT * FROM TABELA_DE_CLIENTES WHERE IDADE <> 18;Copiar código
22) Use datas para filtrar os registros que serão exibidos:

SELECT * FROM TABELA_DE_CLIENTES WHERE DATA_DE_NASCIMENTO >= '14/11/95';Copiar código
23) Para explicitar a data, execute o comando:

SELECT * FROM TABELA_DE_CLIENTES WHERE DATA_DE_NASCIMENTO >= TO_DATE('14/11/1995','DD/MM/YYYY');Copiar código
24) Usando a notação americana, execute o comando:

SELECT * FROM TABELA_DE_CLIENTES WHERE DATA_DE_NASCIMENTO >= TO_DATE('11/14/1995','MM/DD/YYYY');Copiar código
25) Se quiser mostrar dados entre limites, execute BETWEEN:

SELECT * FROM TABELA_DE_CLIENTES WHERE IDADE BETWEEN 17 AND 22;Copiar código
26) Execute o comando abaixo para mostrar os registros com letras em ordem alfabética depois de Lapa:

SELECT * FROM TABELA_DE_CLIENTES WHERE BAIRRO >= 'Lapa';Copiar código
27) Para exercitar os filtros com expressões lógicas compostas, crie um novo script, chamado 2580-video2.5. Abra o ícone Planilha SQL e CONEXAO MAQUINA LOCAL.

28) Entre com os comandos para verificar o uso das expressões lógicas:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR = 'Manga' OR TAMANHO = '470 ml';
SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR = 'Manga' AND TAMANHO = '470 ml';Copiar código
29) Use o NOT com as expressões lógicas:

SELECT * FROM TABELA_DE_PRODUTOS WHERE NOT (SABOR = 'Manga' AND TAMANHO = '470 ml');
SELECT * FROM TABELA_DE_PRODUTOS WHERE NOT (SABOR = 'Manga' OR TAMANHO = '470 ml');Copiar código
30) Os comandos seguintes são equivalentes:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR = 'Manga' OR SABOR = 'Laranja' OR SABOR = 'Melancia';
SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR IN ('Manga','Laranja','Melancia');Copiar código
31) Junte o IN com outra expressão lógica AND:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR IN ('Manga','Laranja','Melancia') AND TAMANHO = '1 Litro';Copiar código
32) Acompanhe as explicações dos comandos lógicos aplicados à tabela TABELA_DE_CLIENTES:

SELECT * FROM TABELA_DE_CLIENTES;
SELECT * FROM TABELA_DE_CLIENTES WHERE CIDADE IN ('Rio de Janeiro','Sao Paulo') AND IDADE >= 20;
SELECT * FROM TABELA_DE_CLIENTES WHERE CIDADE IN ('Rio de Janeiro','Sao Paulo') AND (IDADE >= 20 AND IDADE <= 25);
SELECT * FROM TABELA_DE_CLIENTES WHERE CIDADE IN ('Rio de Janeiro','Sao Paulo') AND (IDADE BETWEEN 20 AND 25);Copiar código
33) Crie um novo script, usando a TABELA_DE_PRODUTOS.

34) Para ver todos os sabores que tem Lima/Limao ou Morango/Limao, execute o comando:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR IN ('Lima/Limao','Morango/Limao');Copiar código
35) Para ver todos os sabores que tem Limao no sabor, execute o comando:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR LIKE '%Limao';Copiar código
36) Use o % nos comandos para buscar os registros com SABOR de Maca:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR LIKE '%Maca%';Copiar código
37) Ao usar o % junto com o comando LIKE, podem ser mostrados resultados diferentes:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR LIKE 'Morango%';
SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR LIKE '%Morango';Copiar código
38) O AND pode ser usado junto com o LIKE, como no comando:

SELECT * FROM TABELA_DE_PRODUTOS WHERE SABOR LIKE 'Morango%' AND EMBALAGEM = 'PET';

Na atividade onde pretendíamos obter os produtos que venderam mais que 394000 litros, executamos esta consulta:

SELECT CODIGO_DO_PRODUTO, SUM(QUANTIDADE) FROM ITENS_NOTAS_FISCAIS 
GROUP BY CODIGO_DO_PRODUTO HAVING SUM(QUANTIDADE) > 394000 
ORDER BY SUM(QUANTIDADE) DESC;