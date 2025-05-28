# Sistema de Clientes e Pedidos (Python + MySQL)

Este é um sistema de cadastro de clientes e seus pedidos utilizando **Python** e **MySQL**, com funcionalidades completas de CRUD e relacionamento entre tabelas. Ideal para quem está aprendendo a usar **JOINs** e relações entre tabelas.

## Funcionalidades

- [x] Cadastrar clientes
- [x] Cadastrar pedidos associados a clientes
- [x] Listar todos os clientes
- [x] Listar todos os pedidos de um cliente específico
- [x] Atualizar nome de um cliente
- [x] Deletar cliente e todos os seus pedidos
- [x] Interface via terminal

## Tecnologias utilizadas

- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python`

## Requisitos

- Ter o **MySQL Server** instalado e em execução
- Ter criado as tabelas no banco de dados com os comandos:

SQL:
    CREATE DATABASE clientes;
    
    USE clientes;
    
    CREATE TABLE nome_clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100)
    );
    
    CREATE TABLE pedidos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        item VARCHAR(100),
        valor FLOAT,
        id_cliente INT,
        FOREIGN KEY (id_cliente) REFERENCES nome_clientes(id) ON DELETE CASCADE
    );

## Instalar o conector do MySQL
  pip install mysql-connector-python

## Como executar
  1. Edite o arquivo e configure os dados de conexão!
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="clientes"
)
  2. Execute o script
     python clientes_e_pedidos(JOINs).py

  3.Use o menu no terminal
    [1] Cadastrar cliente
    [2] Cadastrar pedido
    [3] Listar todos os clientes
    [4] Listar pedidos de um cliente
    [5] Atualizar nome de cliente
    [6] Deletar cliente (e todos seus pedidos)
    [0] Sair
    
## Como funciona o relacionamento
Cada cliente pode ter vários pedidos.

Os pedidos estão vinculados ao cliente por meio do campo id_cliente.

Ao deletar um cliente, todos os seus pedidos são removidos automaticamente (se ON DELETE CASCADE for usado na tabela).
