import sqlite3

conexion=sqlite3.connect("bd1.db")
precio=float(input("Ingrese un precio:"))
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))
filas=cursor.fetchall()
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
conexion.close()
'''
Aquest codi en Python llegeix les dades de la taula “articulos” de la base de dades SQLite “bd1.db” utilitzant un valor ingressat per l’usuari com a criteri de cerca.
La funció “input()” s’utilitza per sol·licitar a l’usuari que ingressi un valor i la funció “float()” s’utilitza per convertir el valor ingressat en un número decimal. 
La funció “execute()” s’utilitza per executar una consulta SQL que selecciona la columna “descripcion” de la taula “articulos” on el preu és menor que el valor ingressat per l’usuari. 
La funció “fetchall()” s’utilitza per obtenir totes les files retornades per la consulta. Si hi ha files retornades, la funció “for” s’utilitza per iterar sobre cada fila i la funció “print()” s’utilitza per imprimir la descripció de cada fila. 
Si no hi ha files retornades, es mostra el missatge “No existen artículos con un precio menor al ingresado.”.
'''
