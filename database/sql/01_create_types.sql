
-- Criação dos tipos ENUM utilizados no sistema
CREATE TYPE tipo_telefone AS ENUM ('CELULAR', 'TRABALHO', 'FIXO');
CREATE TYPE categoria_nome AS ENUM ('ALIMENTOS', 'BELEZA', 'ROUPAS', 'ELETRONICOS', 'BRINQUEDOS');
CREATE TYPE status_pedido AS ENUM ('PENDENTE', 'PAGO', 'ENVIADO','ENTREGUE');