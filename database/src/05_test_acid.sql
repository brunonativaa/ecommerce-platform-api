-- Teste de atomicidade
BEGIN;

INSERT INTO pedido (id_cliente, id_usuario, id_endereco_entrega)
VALUES (1, 1, 1);

-- Deve falhar
INSERT INTO produto_pedido (id_pedido, id_produto, quantidade)
VALUES (999, 1, 2);

COMMIT;
