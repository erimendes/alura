-- Criação da tabela_esquerda
CREATE TABLE tabela_esquerda (
    identificador INT PRIMARY KEY, -- Coluna para o identificador único (chave primária)
    nome VARCHAR(255) NOT NULL    -- Coluna para o nome, não pode ser nulo
);

-- Criação da tabela_direita
CREATE TABLE tabela_direita (
    identificador INT,             -- Coluna para o identificador (chave estrangeira)
    hobby VARCHAR(255),            -- Coluna para o hobby
    -- Define a chave estrangeira que referencia a tabela_esquerda
    FOREIGN KEY (identificador) REFERENCES tabela_esquerda(identificador)
);

-- Exemplo de inserção de dados na tabela_esquerda
INSERT INTO tabela_esquerda (identificador, nome) VALUES
(1, 'João Silva'),
(2, 'Maria Souza'),
(3, 'Pedro Costa');

-- Exemplo de inserção de dados na tabela_direita
INSERT INTO tabela_direita (identificador, hobby) VALUES
(1, 'Leitura'),
(1, 'Caminhada'),
(2, 'Pintura'),
(3, 'Cozinhar'),
(3, 'Jogar Futebol');

-- Exemplo de como você pode juntar as tabelas para ver os dados
-- SELECT
--     te.nome,
--     td.hobby
-- FROM
--     tabela_esquerda AS te
-- JOIN
--     tabela_direita AS td ON te.identificador = td.identificador;
