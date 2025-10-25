import sqlite3 
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

cursor.execute('''

        CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL        
);
            
               ''')


cursor.execute("INSERT INTO alunos('nome','idade','email') VALUES (?,?,?)", ('Lucas','15','luluca@gmail.com'))
cursor.execute("INSERT INTO alunos('nome','idade','email') VALUES (?,?,?)", ('Lara','17','lauana@gmail.com'))
cursor.execute("INSERT INTO alunos('nome','idade','email') VALUES (?,?,?)", ('Lula','79','lulapt@gmail.com'))


conexao.commit()

consulta = cursor.execute("SELECT * FROM alunos")

for lista in consulta.fetchall():
    print(f'name: {lista[1]} - idade: {lista[2]} - email: {lista[3]}')


cursor.execute("UPDATE nome SET idade = ? WHERE id = ?", ('lucas',15))

conexao.commit()

cursor.execute("DELETE from alunos WHERE nome = ?", ('Lara',))
conexao.commit()
conexao.close()