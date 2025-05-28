import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sua_senha_aqui",
    database = "clientes"
)

cursor = conexao.cursor()

# Função para exibir o menu principal
def menu():
    print(''' 
[1] Cadastrar cliente
[2] Cadastrar pedido
[3] Listar todos os clientes
[4] Listar pedidos de um cliente
[5] Atualizar nome de cliente
[6] Deletar cliente (e todos seus pedidos)
[0] Sair''')

# Loop principal
while True:
    menu()
    try:
        escolha = int(input('ESCOLHA:'))
    except:
        print('!&ERRO! digite um número válido!')
        continue

    if escolha == 0:
        print('Volte sempre!')
        break

    elif escolha == 1:
        # CREATE - Cadastrar novo cliente
        nome_do_cliente = input('NOME:')
        comando_cadastrar = 'INSERT INTO nome_clientes (nome) VALUES(%s)'
        adicionar_valores = (nome_do_cliente,)
        cursor.execute(comando_cadastrar, adicionar_valores)
        conexao.commit()
        print('Cliente cadastrado com sucesso!')

    elif escolha == 2:
        # CREATE - Cadastrar pedido de cliente existente
        try:
            id_cliente = int(input('ID do cliente que está fazendo o pedido:'))
        except:
            print('ID inválido!')
            continue

        nome_item = input('Nome do item:')
        try:
            valor_item = float(input('VALOR:'))
        except:
            print('Ocorreu um ERRO, tente novamente!')
            continue

        comando_pedidos = 'INSERT INTO pedidos(item, valor, id_cliente) VALUES (%s,%s,%s)'
        adicionar_valores2 = nome_item, valor_item, id_cliente
        cursor.execute(comando_pedidos, adicionar_valores2)
        conexao.commit()
        print('Pedido adicionado com sucesso!')

    elif escolha == 3:
        # READ - Lista todos os clientes
        comando_read = 'SELECT * FROM nome_clientes'
        cursor.execute(comando_read)
        resultado_leitura = cursor.fetchall()
        for linha in resultado_leitura:
            id = linha[0]
            nome = linha[1]
            print(f'ID: {id} | NOME: {nome}')

    elif escolha == 4:
        # READ - Lista os pedidos de um cliente específico
        try:
            id_cliente_listar = int(input('ID do cliente: '))
        except:
            print('ID inválido!')
            continue

        comando_listar_pedidos = 'SELECT item, valor FROM pedidos WHERE id_cliente = %s'
        cursor.execute(comando_listar_pedidos, (id_cliente_listar,))
        pedidos = cursor.fetchall()

        if not pedidos:
            print('Esse cliente não tem pedidos!')
        else:
            print(f'Pedidos do cliente {id_cliente_listar}')
            for item, valor in pedidos:
                print(f'ITEM: {item} | VALOR: {valor:.2f}R$')

    elif escolha == 5:
        # UPDATE - Atualiza o nome do cliente
        try:
            novo_id = int(input('ID da coluna que será alterada:'))
        except:
            print('Digite um ID válido!')
            continue

        novo_nome2 = input('NOVO NOME:')
        comando_update = 'UPDATE nome_clientes SET nome = %s WHERE id = %s'
        valor_update = novo_nome2, novo_id
        cursor.execute(comando_update, valor_update)
        conexao.commit()
        print('Novo nome atualizado!')

    elif escolha == 6:
        # DELETE - Deleta cliente e todos os seus pedidos
        try:
            id_coluna_delete = int(input('ID da coluna que será apagada:'))
        except:
            print('ID inválido!')
            continue

        comando_delete_pedidos = 'DELETE FROM pedidos WHERE id_cliente = %s'
        cursor.execute(comando_delete_pedidos, (id_coluna_delete,))

        comando_delete_clientes = 'DELETE FROM nome_clientes WHERE id = %s'
        cursor.execute(comando_delete_clientes, (id_coluna_delete,))
        conexao.commit()
        print('Cliente e Pedidos deletados!')

# Encerra a conexão
cursor.close()
conexao.close()
