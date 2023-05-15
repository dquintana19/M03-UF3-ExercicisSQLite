import sqlite3

conexion=sqlite3.connect("bd1.db")
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
conexion.commit()
conexion.close()
'''
Aquest codi a Python insereix tres files a la taula "articles" de la base de dades SQLite "bd1.db". 
La primera fila té "taronges" com a descripció i 23.50 com a preu. 
La segona fila té "peres" com a descripció i 34 com a preu. 
La tercera fila té "bananes" com a descripció i 25 com a preu. 
La funció "commit()" s'utilitza per guardar els canvis a la base de dades i la funció "close()" s'utilitza per tancar la connexió amb la base de dades.
'''