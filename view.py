import sqlite3 as lite

# Função para criar a conexão
def conectar():
    return lite.connect('db.sqlite3')

# Inserir dados na base de dados
def adicionar_categoria_no_bd(nome):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO Categoria(nome) VALUES(?)", (nome,))
            conexion.commit()  # Importante para salvar a transação
            print(f"Categoria '{nome}' adicionada com sucesso.")
    except lite.Error as e:
        print(f"Erro ao inserir categoria: {e}")

# # Inserir categoria 'Alimentação'
# adicionar_categoria_no_bd('Alimentação')

def adicionar_receita_no_bd(categoria_id, adicionado_em, valor):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO Receita(categoria_id, adicionado_em, valor) VALUES(?, ?, ?)', (categoria_id, adicionado_em, valor))
            conexion.commit()  # Importante para salvar a transação
            print(f"Receita adicionada com sucesso.")
    except lite.Error as e:
        print(f"Erro ao inserir receita: {e}")

def adicionar_despesa_no_bd(categoria_id, retirado_em, valor):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO Despesa(categoria_id, retirado_em, valor) VALUES(?, ?, ?)', (categoria_id, retirado_em, valor))
            conexion.commit()  # Importante para salvar a transação
            print(f"Despesa adicionada com sucesso.")
    except lite.Error as e:
        print(f"Erro ao inserir despesa: {e}")

# Deletar dados na base de dados
def deletar_receita(id):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM Receita WHERE id = ?', (id,))
            conexion.commit()  # Importante para confirmar a exclusão
            print(f"Receita com id {id} deletada com sucesso.")
    except lite.Error as e:
        print(f"Erro ao deletar receita: {e}")

def deletar_despesa(id):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM Despesa WHERE id = ?', (id,))
            conexion.commit()  # Importante para confirmar a exclusão
            print(f"Despesa com id {id} deletada com sucesso.")
    except lite.Error as e:
        print(f"Erro ao deletar despesa: {e}")

# Consultar dados na base de dados
def ver_categoria():
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM Categoria')
            return cursor.fetchall()
    except lite.Error as e:
        print(f"Erro ao ver categoria: {e}")

def ver_receita():
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM Receita')
            return cursor.fetchall()
    except lite.Error as e:
        print(f"Erro ao ver receita: {e}")

def ver_despesa():
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM Despesa')
            return cursor.fetchall()
    except lite.Error as e:
        print(f"Erro ao ver despesa: {e}")
