Chegou a hora de você pôr em prática o que foi visto na aula. Para isso, execute os passos listados abaixo.

1) No Oracle SQL Developer, abra outra janela de script e execute o código para mostrar o nome dos clientes:

SELECT NOME FROM TABELA_DE_CLIENTES;Copiar código
2) Para mostrar os nomes em caixa baixa, use o comando LOWER:

SELECT NOME, LOWER(NOME) FROM TABELA_DE_CLIENTESCopiar código
3) Use UPPER para mostrar os caracteres em maiúsculo:

SELECT NOME, LOWER(NOME), UPPER(NOME) FROM TABELA_DE_CLIENTES;Copiar código
4) A função INITCAP coloca cada letra inicial em maiúscula:

SELECT NOME_DO_PRODUTO, INITCAP(NOME_DO_PRODUTO) FROM TABELA_DE_PRODUTOS;Copiar código
5) Para mostrar a rua e bairro de cada registro, execute:

SELECT ENDERECO_1, BAIRRO FROM TABELA_DE_CLIENTES;Copiar código
6) Para concatenar campos do registro, use o comando CONCAT:

SELECT ENDERECO_1, BAIRRO, CONCAT(CONCAT(ENDERECO_1, ' '), BAIRRO) FROM TABELA_DE_CLIENTES;Copiar código
7) Para concatenar vários campos e mostrar o endereço completo, execute:

SELECT ENDERECO_1 || ' ' || BAIRRO || ' ' || CIDADE || ' ' || ESTADO || ' - ' || CEP FROM TABELA_DE_CLIENTES;Copiar código
8) Use o comando LPAD para preencher espaços:

SELECT NOME_DO_PRODUTO, LPAD(NOME_DO_PRODUTO,70,'*') FROM TABELA_DE_PRODUTOS;Copiar código
9) O comando RPAD coloca os asteriscos do lado direito:

SELECT NOME_DO_PRODUTO, RPAD(NOME_DO_PRODUTO,70,'*') FROM TABELA_DE_PRODUTOS;Copiar código
10) O comando SBUSTR mostra o subtexto de uma string:

SELECT NOME_DO_PRODUTO, SUBSTR(NOME_DO_PRODUTO,3,5) FROM TABELA_DE_PRODUTOS;Copiar código
11) Para mostrar quais registros possuem Campo, use o comando INSTR:

SELECT NOME_DO_PRODUTO, INSTR(NOME_DO_PRODUTO,'Campo') FROM TABELA_DE_PRODUTOS;Copiar código
12) Mostre quais registros possuem a palavra Mattos:

SELECT NOME, INSTR(NOME, 'Mattos') FROM TABELA_DE_CLIENTES;Copiar código
13) Use filtro para mostrar os nomes com Mattos:

SELECT NOME FROM TABELA_DE_CLIENTES WHERE INSTR(NOME, 'Mattos') <> 0;Copiar código
14) O LTRIM é usado para remover os caracteres de espaço da extremidade esquerda da palavra:

SELECT '    VICTORINO   ' AS X, LTRIM('    VICTORINO   ') AS Y FROM DUAL;Copiar código
15) Usando o RTRIM e TRIM, você terá:

SELECT '    VICTORINO   ' AS X, LTRIM('    VICTORINO   ') AS Y, RTRIM('    VICTORINO   ') AS Z 
, TRIM('    VICTORINO   ') AS W FROM DUAL;Copiar código
16) O comando REPLACE substitui strings quando mostra os resultados:

SELECT NOME_DO_PRODUTO, REPLACE(REPLACE(NOME_DO_PRODUTO, 'Litro', 'L'), 'Ls', 'L') FROM TABELA_DE_PRODUTOS;Copiar código
17) Crie um novo script e mostre a data do computador:

SELECT SYSDATE FROM DUAL;Copiar código
18) Use a função TO_CHAR para mudar o formato da data:

SELECT TO_CHAR(SYSDATE, 'DD/MM/YYYY HH:MI:SS') FROM DUAL;Copiar código
19) Mostre o nome e data de nascimento da tabela dos clientes:

SELECT NOME, DATA_DE_NASCIMENTO FROM TABELA_DE_CLIENTES;Copiar código
20) Use o TO_CHAR para mudar o formato da data:

SELECT NOME, TO_CHAR(DATA_DE_NASCIMENTO, 'DD MONTH YYYY, DAY') FROM TABELA_DE_CLIENTES;Copiar código
21) Para adicionar números a uma data, use a função SYSDATE:

SELECT SYSDATE + 127 FROM DUAL;Copiar código
22) Para fazer operações entre datas, execute:

SELECT NOME, IDADE, TO_CHAR(DATA_DE_NASCIMENTO, 'DD MONTH YYYY, DAY') FROM TABELA_DE_CLIENTES;Copiar código
23) Para mostrar a idade, execute:

SELECT NOME, IDADE, (SYSDATE - DATA_DE_NASCIMENTO)/365 FROM TABELA_DE_CLIENTES;Copiar código
24) Para mostrar o número de anos, use o comando MONTHS_BETWEEN:

SELECT NOME, IDADE, MONTHS_BETWEEN(SYSDATE, DATA_DE_NASCIMENTO)/12 FROM TABELA_DE_CLIENTES;Copiar código
25) Use o comando ADD_MONTHS para calcular o vencimento das faturas:

SELECT ADD_MONTHS(SYSDATE, 10) FROM DUAL;Copiar código
26) O comando NEXT_DAY mostra a próxima data:

SELECT SYSDATE, NEXT_DAY(SYSDATE, 'SEXTA') FROM DUAL;Copiar código
27) Para mostrar o último dia, use LAST_DAY:

SELECT SYSDATE, LAST_DAY(SYSDATE) FROM DUAL;Copiar código
28) Com o comando TRUNC, mostre o primeiro dia do mês da data especificada:

SELECT SYSDATE + 200, TRUNC(SYSDATE + 200, 'MONTH') FROM DUAL;Copiar código
29) Use o comando ROUND com YEAR para mostrar o primeiro dia do próximo ano:

SELECT SYSDATE, ROUND(SYSDATE, 'YEAR') FROM DUAL;Copiar código
30) Crie um novo script e use o comando FROM DUAL:

SELECT 3.4 FROM DUAL;Copiar código
31) Use o comando ROUND e veja o seu uso, arredondando a resposta:

SELECT ROUND(3.4) FROM DUAL;

SELECT ROUND(3.6) FROM DUAL;

SELECT ROUND(3.5) FROM DUAL;        Copiar código
32) O comando CEIL é usado para retornar o menor inteiro maior que o número:

SELECT CEIL(3.4) FROM DUAL;

SELECT CEIL(3.6) FROM DUAL;

SELECT CEIL(3.5) FROM DUAL;Copiar código
33) O comando POWER eleva o primeiro número pelo segundo:

SELECT POWER(10, 4) FROM DUAL;

SELECT POWER(34, 4) FROM DUAL;Copiar código
34) O EXP faz o exponencial do número:

SELECT EXP(4) FROM DUAL;Copiar código
35) O comando SQRT mostra a raiz quadrada do número:

SELECT SQRT(144) FROM DUAL;

SELECT SQRT(10) FROM DUAL;Copiar código
36) O comando ABS retorna o valor absoluto (positivo):

SELECT ABS(10) FROM DUAL;

SELECT ABS(-10) FROM DUAL;Copiar código
37) O comando MOD exibe o resto da divisão de um valor por outro:

SELECT MOD(10, 6) FROM DUAL;Copiar código
38) Crie um script novo e execute o código EXTRACT, para para converter as datas:

SELECT EXTRACT(MONTH FROM TO_DATE('12/11/2019','DD/MM/YYYY')) FROM DUAL;

SELECT EXTRACT(MONTH FROM TO_DATE('12/11/2019','MM/DD/YYYY')) FROM DUAL;Copiar código
39) Para converter o caractere 10 para o número 10, use o TO_NUMBER:

SELECT TO_NUMBER('10') + 10 FROM DUAL;Copiar código
40) Para converter número para caractere, use TO_CHAR:

SELECT TO_CHAR(1234.123, '9999') FROM DUAL;

SELECT TO_CHAR(1234.123, '9999,999') FROM DUAL;Copiar código
41) Use o comando NVL para substituir o valor NULL por outro valor:

SELECT NVL(10, 0) FROM DUAL;

SELECT NVL(NULL, 0) FROM DUAL;Copiar código
42) Use NVL com comandos FULL JOIN:

SELECT 
NVL(TV.NOME,'NÃO ENCONTRADO') AS NOME_VENDEDOR,
NVL(TV.BAIRRO,'NÃO ENCONTRADO') AS NOME_BAIRRO_VENDEDOR,
NVL(TC.NOME,'NÃO ENCONTRADO') AS NOME_CLIENTE,
NVL(TC.BAIRRO,'NÃO ENCONTRADO') AS NOME_BAIRRO_CLIENTE
FROM
TABELA_DE_VENDEDORES TV
FULL JOIN
TABELA_DE_CLIENTES TC
ON TV.BAIRRO = TC.BAIRRO;