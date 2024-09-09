import sqlite3 as lite

conexion = lite.connect('db.sqlite3')


with conexion:
  cursor = conexion.cursor()
  
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categoria(
      id INTEGER PRIMARY KEY, 
      nome TEXT
    )
  ''')

  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Receita(
      id INTEGER PRIMARY KEY, 
      categoria_id INTEGER, 
      adicionado_em DATE, 
      valor INTEGER,
      FOREIGN KEY(categoria_id) REFERENCES Categoria(id)
    )
  ''')

  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Despesa(
      id INTEGER PRIMARY KEY, 
      categoria_id INTEGER, 
      retirado_em DATE, 
      valor INTEGER,
      FOREIGN KEY(categoria_id) REFERENCES Categoria(id)
    )
  ''')
