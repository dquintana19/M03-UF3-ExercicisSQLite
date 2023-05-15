import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
conexion.close()

'''
Aquest codi a Python crea una taula anomenada "articles" en una base de dades SQLite anomenada "bd1.db".
La taula té tres columnes: "codigo", "descripcion" i "preu". 
La columna "codigo" és la clau primària de la taula i s'incrementa automàticament. 
La columna "descripcion" és de tipus text i la columna "preu" és de tipus real. 
Si la taula ja existeix, el codi imprimirà "La taula ja existeix"
'''