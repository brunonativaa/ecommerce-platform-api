ALTER TABLE cliente
ADD CONSTRAINT cliente_id_usuario_fkey
FOREIGN KEY (id_usuario)
REFERENCES usuario(id_usuario);

ALTER TABLE vendedor
ADD CONSTRAINT vendedor_id_usuario_fkey
FOREIGN KEY (id_usuario)
REFERENCES usuario(id_usuario);

ALTER TABLE endereco
ADD CONSTRAINT endereco_usuario_unique
UNIQUE (id_endereco, id_usuario);

ALTER TABLE pedido
ADD CONSTRAINT fk_endereco_usuario
FOREIGN KEY (id_endereco_entrega, id_usuario)
REFERENCES endereco(id_endereco, id_usuario);

ALTER TABLE produto
ADD CONSTRAINT produto_id_vendedor_fkey
FOREIGN KEY (id_vendedor)
REFERENCES vendedor(id_vendedor);

ALTER TABLE estoque
ADD CONSTRAINT estoque_id_produto_fkey
FOREIGN KEY (id_produto)
REFERENCES produto(id_produto);

ALTER TABLE produto_pedido
ADD CONSTRAINT produto_pedido_id_pedido_fkey
FOREIGN KEY (id_pedido)
REFERENCES pedido(id_pedido);

ALTER TABLE produto_pedido
ADD CONSTRAINT produto_pedido_id_produto_fkey
FOREIGN KEY (id_produto)
REFERENCES produto(id_produto);
