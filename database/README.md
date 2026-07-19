## 📐 Modelagem do E-commerce

<i>Imagem do diagrama:</i>
![Diagrama E-commerce](./docs/eccomerce.png)

### 📐 Decisões de Arquitetura e Modelagem (ShopWave)

- **Modelagem de Supertipo/Subtipo (Usuários):** Criei a entidade central `Usuario` (detentora das credenciais de acesso), ramificando-a nas tabelas `Cliente` e `Vendedor` por meio de relacionamentos 1:1. Essa abordagem de subtipagem permite que um usuário atue como cliente, vendedor ou **ambos** simultaneamente no ecossistema, sem duplicar dados confidenciais ou gerar campos nulos desnecessários.
- **Flexibilidade de Cadastro (1FN):** Ao vincular as tabelas de `Endereco` e `Telefone` diretamente ao `id_usuario` (em relacionamentos 1:N), o sistema cumpre a Primeira Forma Normal de maneira escalável, permitindo múltiplos endereços de entrega e contatos por usuário.
- **Resolução de Relacionamento Muitos para Muitos (N:N):** Um pedido pode conter múltiplos produtos, e um produto pode constar em múltiplos pedidos. Para resolver essa cardinalidade complexa, criei a tabela associativa `Produto_Pedido`. Ela atua como entidade composta armazenando as chaves estrangeiras (`id_pedido` e `id_produto`), além de "congelar" a `quantidade` e o `preco_unitario_pago` no momento exato da transação, blindando o histórico financeiro contra reajustes futuros no catálogo do vendedor.
- **Isolamento de Estado Volátil (Estoque):** A quantidade de itens disponíveis foi isolada na tabela `Estoque` ligada em 1:1 com `Produto`, garantindo integridade e alta performance em operações frequentes de escrita e atualização de dados de inventário.
