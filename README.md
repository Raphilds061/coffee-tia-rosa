☕ Sistema: [c̲̅σ̲̅f̲̅f̲̅є̲̅є̲̅-̲̅т̲̅i̲̅α̲̅-̲̅я̲̅σ̲̅s̲̅α̲̅]

📌 Objetivo 📌
Gerenciar de forma simples e eficiente:

Produtos da cafeteria;
Clientes;
Pedidos;
Relatórios de vendas.

🧱 Estrutura dos Arquivos 🧱

O sistema armazena dados em 3 arquivos .json, para manter a persistência das informações:

produtos.json → Armazena os produtos do cardápio

clientes.json → Armazena os dados dos clientes

pedidos.json → Guarda o histórico de pedidos realizados

🔧 Funcionalidades Principais 🔧

1. Cadastrar Produto
   
Solicita nome, preço e ingredientes

Salva no arquivo produtos.json

Permite vários ingredientes separados por vírgula

2. Visualizar Cardápio

Exibe todos os produtos cadastrados com:

Nome;
Preço;
Ingredientes.

3. Cadastrar Cliente

Solicita nome, CPF, número de telefone e email.

Salva no arquivo clientes.json

4. Realizar Pedido

Lista todos os clientes e produtos disponíveis

Permite selecionar cliente e produtos

Calcula o total do pedido

Salva o pedido completo no arquivo pedidos.json

5. Relatório de Vendas

Mostra:

Valor total arrecadado com pedidos

Quantidade total de pedidos registrados

6. Menu Interativo

Interface de texto simples

Opções numeradas para facilitar o uso

Loop contínuo até que o usuário escolha "Sair"

<img width="1024" height="768" alt="image" src="https://github.com/user-attachments/assets/c2216509-5e59-4c36-a51f-dc75b1de5640" />
