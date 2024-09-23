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

# def deletar():
#     try:
#         treev_dados = tree.focus()
#         treev_dicionario = tree.item(treev_dados)
#         treev_lista = treev_dicionario['values']
#         valor = treev_lista[0]

#         deletar_form([valor])

#         messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

#         for widget in frameDireita.winfo_children():
#             widget.destroy()

#         mostrar()

#     except IndexError:
#         messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

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

def tabela():
    gastos = ver_despesa()
    receitas = ver_receita()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

# # Função para deletar a categoria
# def deletar_categoria(nome_categoria):
#     conn = conectar()
#     cursor = conn.cursor()

#     try:
#         # Executa a instrução SQL para deletar a categoria pelo nome
#         cursor.execute("DELETE FROM categoria WHERE nome = ?", (nome_categoria,))
#         conn.commit()  # Aplica as alterações
#         print(f"Categoria '{nome_categoria}' deletada com sucesso!")
#     except lite.Error as erro:
#         print(f"Erro ao deletar categoria: {erro}")
#     finally:
#         conn.close()  # Fecha a conexão com o banco de dados

# # Exemplo de uso
# categoria_a_deletar = "Alimentação"  # Substitua pelo nome da categoria que deseja deletar
# deletar_categoria(categoria_a_deletar)