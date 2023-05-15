import sqlite3

conexion=sqlite3.connect("bd1.db")
codigo=int(input("Ingrese el código de un artículo:"))
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))
fila=cursor.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()
'''
Aquest codi en Python crea una taula anomenada “articulos” en una base de dades SQLite anomenada “bd1.db”.
La taula té tres columnes: “codigo”, “descripcion” i “precio”. 
La columna “codigo” és la clau primària de la taula i s’incrementa automàticament. 
Aquest codi en Python insereix tres files a la taula “articulos” de la base de dades SQLite “bd1.db”. 
La primera fila té “naranjas” com a descripció i 23.50 com a preu. La segona fila té “peras” com a descripció i 34 com a preu. 
La tercera fila té “bananas” com a descripció i 25 com a preu. 
Aquest codi en Python llegeix les dades de la taula “articulos” de la base de dades SQLite “bd1.db”. 
La funció “execute()” s’utilitza per executar una consulta SQL que selecciona les columnes “codigo”, “descripcion” i “precio” de la taula “articulos”. 
La funció “for” s’utilitza per iterar sobre cada fila retornada per la consulta i la funció “print()” s’utilitza per imprimir cada fila. 
Aquest codi en Python llegeix les dades de la taula “articulos” de la base de dades SQLite “bd1.db” utilitzant un valor ingressat per l’usuari com a criteri de cerca. 
La funció “input()” s’utilitza per sol·licitar a l’usuari que ingressi un valor i la funció “int()” s’utilitza per convertir el valor ingressat en un número enter.
'''