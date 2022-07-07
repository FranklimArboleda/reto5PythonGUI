# --------- Importar módulos ---------
import sqlite3


# ---------- Clase principal ----------
class Productos:

   # Abrir conexión con la BD
   def abrir(self):
      conexion=sqlite3.connect('tienda.db')
      return conexion

   
   # Inserta en la BD en registro
   def guardar(self, datos):
      conex=self.abrir()
      cursor = conex.cursor()
      sql='INSERT INTO productos(nombre, precio, inventario) values (?, ?, ?)'
      cursor.execute(sql, datos)
      conex.commit()
      conex.close()
   

   # Actualizar un registro de la BD
   def actualizar(self, datos):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='UPDATE productos SET nombre=?, precio=?, inventario=? WHERE codigo=?'
         cursor.execute(sql, datos)
         conex.commit()
      finally:
         conex.close()


   # Eliminar un registro de la BD
   def borrar(self, datos):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='DELETE FROM productos WHERE codigo=? and nombre=? and precio=? and inventario=?'
         cursor.execute(sql, datos)
         conex.commit()
      finally:
         conex.close()


   # Consultar todos los registros de la tabla 'productos'
   def listarTodos(self):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='SELECT codigo, nombre, precio, inventario FROM productos'
         cursor.execute(sql)
         return cursor.fetchall()
      finally:
         conex.close()
   

   # Consultar un registro de la BD
   def consultar(self, datos):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='SELECT * FROM productos WHERE codigo=?'
         cursor.execute(sql, datos)
         return cursor.fetchall()
      finally:
         conex.close()


   # Consultar el nombre del producto con el mayor precio
   def nombrePrecioMayor(self):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='SELECT nombre FROM productos WHERE precio = (SELECT MAX(precio) FROM productos)'
         cursor.execute(sql)
         return cursor.fetchall()
      finally:
         conex.close()


   # Consultar el nombre del producto con el menor precio
   def nombrePrecioMenor(self):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='SELECT nombre FROM productos WHERE precio = (SELECT MIN(precio) FROM productos)'
         cursor.execute(sql)
         return cursor.fetchall()
      finally:
         conex.close()

   
   # Consultar el promedio de la columna precio
   def precioPromedio(self):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='SELECT AVG(precio) FROM productos'
         cursor.execute(sql)
         return cursor.fetchall()
      finally:
         conex.close()


   # Seleccinar el precio y el inventario(cantidad), con esos datos se genera el inventario total
   def inventarioTotal(self):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='SELECT precio, inventario FROM productos'
         cursor.execute(sql)
         return cursor.fetchall()
      finally:
         conex.close()


   # Eliminar todos los registros de una tabla, el nombre de la tabla se pasa por parametro
   def limpiarTabla(self, nombreTabla):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql=f'DELETE FROM {nombreTabla}'
         cursor.execute(sql)
         conex.commit()
      finally:
         conex.close()


   # Insertar en la BD los datos iniciales para poder trabajar sobre la BD
   def llenarTablaProductos(self):
      try:
         conex=self.abrir()
         cursor=conex.cursor()
         sql='''
            INSERT INTO productos (nombre, precio, inventario) VALUES
            ('Manzanas', 5000, 25),
            ('Limones', 2300, 15),
            ('Peras', 2700, 33),
            ('Arandanos', 9300, 5),
            ('Tomates', 2100, 42),
            ('Fresas', 4100, 3),
            ('Helado', 4500, 41),
            ('Galletas', 500, 8),
            ('Chocolates', 3500, 80),
            ('Jamon', 15000, 10)
         '''
         cursor.execute(sql)
         conex.commit()
      finally:
         conex.close()
