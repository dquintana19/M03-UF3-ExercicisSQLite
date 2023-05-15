import sqlite3

conexion=sqlite3.connect("bd1.db")
cursor=conexion.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()

'''
Aquest codi a Python llegeix les dades de la taula "articles" de la base de dades SQLite "bd1.db".
La funció "execute()" s'utilitza per executar una consulta SQL que selecciona les columnes "codigo", "descripcion" i "preu" de la taula "articles".
La funció "for" s'utilitza per iterar sobre cada fila retornada per la consulta i la funció "print()" s'utilitza per imprimir cada fila. 
La funció "close()" s'utilitza per tancar la connexió amb la base de dades.
''' 