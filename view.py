import sqlite3 as lite

# Função para criar a conexão
def conectar():
    return lite.connect('db.sqlite3')

# Inserir dados na base de dados
def inserir_categoria(nome):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO Categoria(nome) VALUES(?)", (nome,))
    except lite.Error as e:
        print(f"Erro ao inserir categoria: {e}")

inserir_categoria('Alimentação')

def inserir_receita(categoria_id, adicionado_em, valor):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO Receita(categoria_id, adicionado_em, valor) VALUES(?, ?, ?)', (categoria_id, adicionado_em, valor))
    except lite.Error as e:
        print(f"Erro ao inserir receita: {e}")

def inserir_despesa(categoria_id, retirado_em, valor):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO Despesa(categoria_id, retirado_em, valor) VALUES(?, ?, ?)', (categoria_id, retirado_em, valor))
    except lite.Error as e:
        print(f"Erro ao inserir despesa: {e}")

# Deletar dados na base de dados
def deletar_receita(id):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM Receita WHERE id = ?', (id,))
    except lite.Error as e:
        print(f"Erro ao deletar receita: {e}")

def deletar_despesa(id):
    try:
        with conectar() as conexion:
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM Despesa WHERE id = ?', (id,))
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



print(ver_categoria())
