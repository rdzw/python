INSERT INTO cidades (nome,are,estado_id)
VALUES ('campinas', 795,31)

INSERT INTO cidades (nome, are, estado_id)
VALUES ('niteroi', 133,25)

INSERT INTO cidades (nome, are, estado_id)
VALUES (
    'caruaru', 
    920.6,
    (select id from estados where sigla = 'PE')
)


select * from cidades