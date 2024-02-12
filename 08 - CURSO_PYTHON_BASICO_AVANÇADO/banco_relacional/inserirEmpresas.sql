alter table empresas modify cnpj varchar(14);

insert into empresas
    (nome, cnpj)
values
    ('bradesco',65464646456),
    ('vale',54646464882),
    ('cielo',787891005574);

desc empresas;
desc prefeitos;

insert into empresas_unidades
        (empresa_id, cidade_id, sede)
values
    (1,1,1),
    (1,2,0),
    (2,1,0),
    (2,2,1);