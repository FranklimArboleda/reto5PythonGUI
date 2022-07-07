'''


 ___ ventana ________________________________________________________________________
|                                                                                   |
| MINIMARKET MINTIC                                                                 |
|___________________________________________________________________________________|
|                                                                                   |
|   ____ labelFrameProductos ____________________________________________________   |
|  |                                                                             |  |
|  |   ___ scrolledTextListado ________________________________________________  |  |
|  |  |                                                                       |  |  |
|  |  |  CODIGO      NOMBRE      PRECIO      INVENTARIO                       |  |  |
|  |  |                                                                       |  |  |
|  |  |     1                                                                 |  |  |
|  |  |     2                                                                 |  |  |
|  |  |     3                                                                 |  |  |
|  |  |     4                                                                 |  |  |
|  |  |     5                                                                 |  |  |
|  |  |     6                                                                 |  |  |
|  |  |     7                                                                 |  |  |
|  |  |     8                                                                 |  |  |
|  |  |     9                                                                 |  |  |
|  |  |    10                                                                 |  |  |
|  |  |_______________________________________________________________________|  |  |
|  |                                                                             |  |
|  |                              ___ botonResetear ________                     |  |
|  |                             |                          |                    |  |
|  |                             |        Resetear BD       |                    |  |
|  |                             |__________________________|                    |  |
|  |_____________________________________________________________________________|  |
|                                                                                   |
|                                                                                   |
|   _________________________________________                                       |
|  |           |               |            |                                       |
|  |  AGREGAR  |  ACTUALIZAR   |   BORRAR   |                                       |
|  |___________|_______________|____________|____________________________________   |
|  |                                                                             |  |
|  |                                                                             |  |
|  |                                                                             |  |
|  |                                                                             |  |
|  |                                                                             |  |
|  |                                                                             |  |
|  |                                                                             |  |
|  |                                                                             |  |
|  |                                                                             |  |
|  |                                                                             |  |
|  |_____________________________________________________________________________|  |
|                                                                                   |
|                                                                                   |
|   ___ labelFrameRespuesta _____________________________________________________   |
|  |                                                                             |  |
|  |   ___ scrolledTextListado _______________________________________________   |  |
|  |  |                                                                       |  |  |
|  |  |                                                                       |  |  |
|  |  |_______________________________________________________________________|  |  |
|  |                                                                             |  |
|  |_____________________________________________________________________________|  |
|                                                                                   |
|___________________________________________________________________________________|

'''


# ---------- Importar módulos ---------
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from turtle import width

# ---------- Importar backend ----------
import productos


# ---------- Clase principal ----------
class Formulario:
   def __init__(self):
      self.producto=productos.Productos()                                                    # Instancia del backend

      self.ventana=tk.Tk()                                                                   # Crear ventana
      self.ventana.title('Minimarket MIN-TIC')                                                  # Definir título a la ventana

      # ----- LabelFrame: listado de productos -----
      self.labelFrameProductos=ttk.LabelFrame(self.ventana, text='Productos')                # Crear LabelFrame 'Productos'
      self.label_frame_productos()                                                              # Función para crear GUI que comforma el LabelFrame 'Productos'
      self.labelFrameProductos.grid(column=0, row=0, padx=10, pady=10)                          # Posicionar labelFrame y se define las distancias con los otros elementos
      self.labelFrameProductos['padding']=(25, 10)                                              # Padding del 'LabelFrame'

      # ----- Notebook: Pestañas (GUARDAR, ACTUALIZAR, BORRAR) -----
      self.cuaderno=ttk.Notebook(self.ventana)                                               # Crear cuaderno
      self.pestana_agregar()                                                                    # Funciones para crear las GUI de las pestañas
      self.pestana_actualizar()
      self.pestana_borrar()
      # self.pestana_casos_prueba()
      self.cuaderno.grid(column=0, row=1, padx=10, pady=10)                                     # Posicionar el cuaderno

      self.labelFrameRespuesta=ttk.LabelFrame(self.ventana, text='Respuesta')                # LabelFrame
      self.label_frame_respuesta()                                                              # Función para crear GUI
      self.labelFrameRespuesta.grid(column=0, row=2, padx=10, pady=4)
      self.labelFrameRespuesta['padding']=(25, 10)

      self.ventana.mainloop()                                                                # Mostrar ventana


   def label_frame_productos(self):
      self.scrolledTextListado=st.ScrolledText(self.labelFrameProductos, width=60, height=15)                                          # ScrollText del listado de productos, se define ancho y alto
      self.scrolledTextListado.grid(column=0, row=0, padx=10, pady=10)

      self.botonResetear=ttk.Button(self.labelFrameProductos, text='Resetear BD', command=self.resetearBD, width=20)                   # Boton que ejecutará la función 'resetearBD()
      self.botonResetear.grid(column=0, row=1, padx=4, pady=4)

      respuesta=self.producto.listarTodos()                                                                                            # Función del script 'productos.py' que retorna todos los productos
      self.actualizarVista(respuesta)                                                                                                  # Función para renderizar los productos en el 'LabelFrame', primera vez que ocurre
   
   def actualizarVista(self, respuesta):                                                                                                              # Refresca el listado de productos
      self.scrolledTextListado.delete('1.0', tk.END)                                                                                                     # Borra contenido del lienzo 'LabelFrame'
      self.scrolledTextListado.insert(tk.END, '============================================================\n')                                          # Renderiza el encabezado del lienzo
      self.scrolledTextListado.insert(tk.END, 'CODIGO\t\tNOMBRE\t\tPRECIO\t\tINVENTARIO\n')
      self.scrolledTextListado.insert(tk.END, '============================================================\n\n')
      for fila in respuesta:                                                                                                                             # Recorre la tupla recibida con los productos y la renderiza en el lienzo
         self.scrolledTextListado.insert(tk.END, '  '+str(fila[0])+'\t\t'+fila[1]+'\t\t'+str(fila[2])+'\t\t    '+str(fila[3])+'\n\n')


   def resetearBD(self):                                                      # Función que resetea la BD con los datos iniciales
      self.producto.limpiarTabla('productos')                                    # Función del script 'productos.py' que borra contenido de la tabla pasada por parametro (productos)
      self.producto.llenarTablaProductos()                                       # Función del script 'productos.py' que inserta los 10 registros iniciales
      respuesta=self.producto.listarTodos()                                      # Función del script 'productos.py' que consulta todos los productos
      self.actualizarVista(respuesta)                                            # Función que actualiza el listado de productos en el lienzo pasansole la tupla de productos como parametro
      self.actualizarRespuesta()                                                 # Función que actualiza la respuesta final de acuerdo al contenido de la BD y a las operaciones (GUAR, ACTU, BORR)


   def label_frame_respuesta(self):
      self.scrolledTextRespuesta=st.ScrolledText(self.labelFrameRespuesta, width=60, height=3)
      self.scrolledTextRespuesta.grid(column=0, row=0, padx=4, pady=4)
      self.actualizarRespuesta()


   def actualizarRespuesta(self):                                                                     # Función que actualiza la respuesta que se muestra en en lienzo pequeño
      registrosConsulta=self.producto.listarTodos()                                                   # Verificamos que haya al menos 1 registro en la BD para que no genere un error al realizar la consulta
      if len(registrosConsulta) > 0:                                                                  # Si existe al menos un registro en la tabla
         nombreMayor=self.producto.nombrePrecioMayor()                                                   # Realizamos 3 de las 4 respuestas que debemos mosrar al final
         nombreMenor=self.producto.nombrePrecioMenor()
         promedio=self.producto.precioPromedio()
         pro=promedio[0]                                                                                 # La respuesta emitida por la BD es una tupla, ese valor lo asignamos a una variable para evitar conflictos el pegarlo el lienzo
         
         inventarioTotal = 0                                                                             # Variable para guardar el inventario total
         registrosParaInventario=self.producto.inventarioTotal()                                         # Función del script 'productos.py', nos retorna una tupla con los precios y cantidades (inventario)
         for registro in registrosParaInventario:
            inventarioTotal+=registro[0]*registro[1]                                                        # Acumulamos el valor del inventario total

         self.scrolledTextRespuesta.delete('1.0', tk.END)                                                # Renderizamos las respuestas en el lienzo pequeño
         self.scrolledTextRespuesta.insert(tk.END, '\n\t\t')
         self.scrolledTextRespuesta.insert(tk.END, nombreMayor[0])                                       # Tomamos el valor de la posición cero [0], a veces encontramos más de una con el mismo valor
         self.scrolledTextRespuesta.insert(tk.END, ' ')
         self.scrolledTextRespuesta.insert(tk.END, nombreMenor[0])
         self.scrolledTextRespuesta.insert(tk.END, ' ')
         self.scrolledTextRespuesta.insert(tk.END, round(pro[0], 1))                                     # Redondeamos a un solo decimal
         self.scrolledTextRespuesta.insert(tk.END, ' ')
         self.scrolledTextRespuesta.insert(tk.END, round(inventarioTotal, 1))
      else:                                                                         # Si la tabla 'productos' está vacia
         self.scrolledTextRespuesta.delete('1.0', tk.END)
         self.scrolledTextRespuesta.insert(tk.END, '\n\t\tLa tabla productos está vacia')


   def pestana_agregar(self):
      # ----- Pestaña 1: AGREGAR -----
      self.pestanaGuardar=ttk.Frame(self.cuaderno)
      self.pestanaGuardar['padding']=(87, 5)                            # Padding de la pestaña
      self.cuaderno.add(self.pestanaGuardar, text='AGREGAR')

      # --- LabelFrame ---
      self.labelFrameProductoGuardar=ttk.LabelFrame(self.pestanaGuardar, text='Producto')
      self.labelFrameProductoGuardar['padding']=(35, 8)                 # Padding del 'LabelFrame'
      self.labelFrameProductoGuardar.grid(column=0, row=0, padx=10, pady=10)

      self.labelNombreGuardar=ttk.Label(self.labelFrameProductoGuardar, text='Nombre:')
      self.labelNombreGuardar.grid(column=0, row=0, padx=4, pady=4)
      self.datosNombreGuardar=tk.StringVar()
      self.entryNombreGuardar=ttk.Entry(self.labelFrameProductoGuardar, textvariable=self.datosNombreGuardar, width=40)
      self.entryNombreGuardar.grid(column=1, row=0, padx=4, pady=4)
      self.entryNombreGuardar.focus_set()                                        # Establecer el foco en esta caja de texto

      self.labelPrecioGuardar=ttk.Label(self.labelFrameProductoGuardar, text='Precio:')
      self.labelPrecioGuardar.grid(column=0, row=1, padx=4, pady=4)
      self.datosPrecioGuardar=tk.StringVar()
      self.entryPrecioGuardar=ttk.Entry(self.labelFrameProductoGuardar, textvariable=self.datosPrecioGuardar, width=40)
      self.entryPrecioGuardar.grid(column=1, row=1, padx=4, pady=4)

      self.labelInventarioGuardar=ttk.Label(self.labelFrameProductoGuardar, text='Inventario:')
      self.labelInventarioGuardar.grid(column=0, row=2, padx=4, pady=4)
      self.datosInventarioGuardar=tk.StringVar()
      self.entryInventarioGuardar=ttk.Entry(self.labelFrameProductoGuardar, textvariable=self.datosInventarioGuardar, width=40)
      self.entryInventarioGuardar.grid(column=1, row=2, padx=4, pady=4)

      self.botonGuardar=ttk.Button(self.labelFrameProductoGuardar, text='Guardar', command=self.guardar, width=20)
      self.botonGuardar.grid(column=1, row=3, padx=20, pady=4)


   def guardar(self):
      if self.datosNombreGuardar.get() == '' or self.datosPrecioGuardar.get() == '' or self.datosInventarioGuardar.get() == '':        # Valida que se ingresen todos los datos
         mb.showwarning('Alerta', 'Para ingresar un producto debe diligenciar todos los datos')
      else:
         datos=(self.datosNombreGuardar.get(), self.datosPrecioGuardar.get(), self.datosInventarioGuardar.get())
         self.producto.guardar(datos)
         mb.showinfo('Información', 'El registro fue guardado con exito')
         self.datosNombreGuardar.set('')
         self.datosPrecioGuardar.set('')
         self.datosInventarioGuardar.set('')

         respuesta=self.producto.listarTodos()                    # Vuelve a llamar la función que lista todos los productos para verlo de inmediato
         self.actualizarVista(respuesta)

         self.actualizarRespuesta()                               # Actualiza la vista de la respuesta


   def pestana_actualizar(self):
      # ----- Pestaña 2: ACTUALIZAR -----
      self.pestanaActualizar=ttk.Frame(self.cuaderno)
      self.pestanaActualizar['padding']=(120, 5)
      self.cuaderno.add(self.pestanaActualizar, text='ACTUALIZAR')

      # --- LabelFrame ---
      self.labelFrameProductoActualizar=ttk.LabelFrame(self.pestanaActualizar, text='Producto')
      self.labelFrameProductoActualizar.grid(column=0, row=0, padx=10, pady=10)

      self.labelCodigoActualizar=ttk.Label(self.labelFrameProductoActualizar, text='Código: ')
      self.labelCodigoActualizar.grid(column=0, row=0, padx=4, pady=4)
      self.datosCodigoActualizar=tk.StringVar()
      self.entryCodigoActualizar=ttk.Entry(self.labelFrameProductoActualizar, textvariable=self.datosCodigoActualizar, width=40)
      self.entryCodigoActualizar.grid(column=1, row=0, padx=4, pady=4)
      

      self.labelNombreActualizar=ttk.Label(self.labelFrameProductoActualizar, text='Nombre:')
      self.labelNombreActualizar.grid(column=0, row=1, padx=4, pady=4)
      self.datosNombreActualizar=tk.StringVar()
      self.entryNombreActualizar=ttk.Entry(self.labelFrameProductoActualizar, textvariable=self.datosNombreActualizar, width=40)
      self.entryNombreActualizar.grid(column=1, row=1, padx=4, pady=4)

      self.labelPrecioActualizar=ttk.Label(self.labelFrameProductoActualizar, text='Precio:')
      self.labelPrecioActualizar.grid(column=0, row=2, padx=4, pady=4)
      self.datosPrecioActualizar=tk.StringVar()
      self.entryPrecioActualizar=ttk.Entry(self.labelFrameProductoActualizar, textvariable=self.datosPrecioActualizar, width=40)
      self.entryPrecioActualizar.grid(column=1, row=2, padx=4, pady=4)

      self.labelInventarioActualizar=ttk.Label(self.labelFrameProductoActualizar, text='Inventario:')
      self.labelInventarioActualizar.grid(column=0, row=3, padx=4, pady=4)
      self.datosInventarioActualizar=tk.StringVar()
      self.entryInventarioActualizar=ttk.Entry(self.labelFrameProductoActualizar, textvariable=self.datosInventarioActualizar, width=40)
      self.entryInventarioActualizar.grid(column=1, row=3, padx=4, pady=4)

      self.botonActualizar=ttk.Button(self.labelFrameProductoActualizar, text='Actualizar', command=self.actualizar, width=20)
      self.botonActualizar.grid(column=1, row=4, padx=20, pady=4)


   def actualizar(self):
      if self.datosCodigoActualizar.get() == '' or self.datosNombreActualizar.get() == '' or self.datosPrecioActualizar.get() == '' or self.datosInventarioActualizar.get() == '':
         mb.showwarning('Alerta', 'Para actualizar un producto debe diligenciar todos los datos')
      else:
         dato=(self.datosCodigoActualizar.get(), )                 # Código para buscar el producto en la bd, (codigo, ), debe ser una tupla
         registro=self.producto.consultar(dato)                # Función que busca el producto en la bd
         if len(registro) > 0:                                 # Si encontró el producto
            datos=(self.datosNombreActualizar.get(), self.datosPrecioActualizar.get(), self.datosInventarioActualizar.get(), self.datosCodigoActualizar.get())
            self.producto.actualizar(datos)
            mb.showinfo('Información', 'El registro fue actualizado con éxito')
            self.datosCodigoActualizar.set('')                                         # Limpiar variables
            self.datosNombreActualizar.set('')
            self.datosPrecioActualizar.set('')
            self.datosInventarioActualizar.set('')

            respuesta=self.producto.listarTodos()                                      # Actualizar vista de los productos
            self.actualizarVista(respuesta)

            self.actualizarRespuesta()                                                 # Actualizar vista de la respuesta
         else:                                                 # Si no encontró el producto
            mb.showwarning('Alerta', 'El producto no existe')
            self.entryCodigoActualizar.delete(0, 'end')
            self.entryNombreActualizar.delete(0, 'end')
            self.entryPrecioActualizar.delete(0, 'end')
            self.entryInventarioActualizar.delete(0, 'end')


   def pestana_borrar(self):
      # ----- Pestaña 3: BORRAR -----
      self.pestanaBorrar=ttk.Frame(self.cuaderno)
      self.pestanaBorrar['padding']=(120, 5)
      self.cuaderno.add(self.pestanaBorrar, text='BORRAR')

      # --- LabelFrame ---
      self.labelFrameProductoBorrar=ttk.LabelFrame(self.pestanaBorrar, text='Producto')
      self.labelFrameProductoBorrar.grid(column=0, row=0, padx=10, pady=10)

      self.labelCodigoBorrar=ttk.Label(self.labelFrameProductoBorrar, text='Código: ')
      self.labelCodigoBorrar.grid(column=0, row=0, padx=4, pady=4)
      self.datosCodigoBorrar=tk.StringVar()
      self.entryCodigoBorrar=ttk.Entry(self.labelFrameProductoBorrar, textvariable=self.datosCodigoBorrar, width=40)
      self.entryCodigoBorrar.grid(column=1, row=0, padx=4, pady=4)
      

      self.labelNombreBorrar=ttk.Label(self.labelFrameProductoBorrar, text='Nombre:')
      self.labelNombreBorrar.grid(column=0, row=1, padx=4, pady=4)
      self.datosNombreBorrar=tk.StringVar()
      self.entryNombreBorrar=ttk.Entry(self.labelFrameProductoBorrar, textvariable=self.datosNombreBorrar, width=40)
      self.entryNombreBorrar.grid(column=1, row=1, padx=4, pady=4)

      self.labelPrecioBorrar=ttk.Label(self.labelFrameProductoBorrar, text='Precio:')
      self.labelPrecioBorrar.grid(column=0, row=2, padx=4, pady=4)
      self.datosPrecioBorrar=tk.StringVar()
      self.entryPrecioBorrar=ttk.Entry(self.labelFrameProductoBorrar, textvariable=self.datosPrecioBorrar, width=40)
      self.entryPrecioBorrar.grid(column=1, row=2, padx=4, pady=4)

      self.labelInventarioBorrar=ttk.Label(self.labelFrameProductoBorrar, text='Inventario:')
      self.labelInventarioBorrar.grid(column=0, row=3, padx=4, pady=4)
      self.datosInventarioBorrar=tk.StringVar()
      self.entryInventarioBorrar=ttk.Entry(self.labelFrameProductoBorrar, textvariable=self.datosInventarioBorrar, width=40)
      self.entryInventarioBorrar.grid(column=1, row=3, padx=4, pady=4)

      self.botonBorrar=ttk.Button(self.labelFrameProductoBorrar, text='Borrar', command=self.borrar, width=20)
      self.botonBorrar.grid(column=1, row=4, padx=20, pady=4)
   

   def borrar(self):
      if self.datosCodigoBorrar.get()=='' or self.datosNombreBorrar.get()=='' or self.datosPrecioBorrar.get()=='' or self.datosInventarioBorrar.get()=='':
         mb.showwarning('Alerta', 'Para eliminar un producto debe ingresar todos los datos')
      else:
         dato=(self.datosCodigoBorrar.get(), )                 # Debe enviar una tupla, (codigo, )
         registro=self.producto.consultar(dato)

         if len(registro) > 0:                                    # Si existe el producto
            datos=(self.datosCodigoBorrar.get(), self.datosNombreBorrar.get(), self.datosPrecioBorrar.get(), self.datosInventarioBorrar.get())
            self.producto.borrar(datos)
            mb.showinfo('Información', 'El producto fue eliminado con éxito')
            self.datosCodigoBorrar.set('')
            self.datosNombreBorrar.set('')
            self.datosPrecioBorrar.set('')
            self.datosInventarioBorrar.set('')

            respuesta=self.producto.listarTodos()                 # Actualizar vista de los productos
            self.actualizarVista(respuesta)

            self.actualizarRespuesta()                                                 # Actualizar vista de la respuesta
         else:                                                    # Si no existe el producto
            mb.showinfo('Alerta', 'El producto no existe')
            self.entryCodigoBorrar.delete(0, 'end')               # Limpiar las cajas de texto despues de no encontrar el registro
            self.entryNombreBorrar.delete(0, 'end')
            self.entryPrecioBorrar.delete(0, 'end')
            self.entryInventarioBorrar.delete(0, 'end')

            self.entryCodigoBorrar.focus_set()

            self.scrolledTextRespuesta.delete('1.0', tk.END)
            self.scrolledTextRespuesta.insert(tk.END, '\n\t\t\tERROR')

'''
   def pestana_casos_prueba(self):
      # ----- Pestaña 4: CASOS DE PRUEBA -----
      self.pestanaCasosPrueba=ttk.Frame(self.cuaderno)
      self.pestanaCasosPrueba['padding']=(20, 5)
      self.cuaderno.add(self.pestanaCasosPrueba, text='CASOS DE PRUEBA')

      # --- LabelFrame ---
      self.labelFrameCasosPrueba=ttk.LabelFrame(self.pestanaCasosPrueba, text='Casos de prueba')
      self.labelFrameCasosPrueba['padding']=(10, 10)
      self.labelFrameCasosPrueba.grid(column=0, row=0, padx=10, pady=10)

      self.labelOperacionCasosPrueba=ttk.Label(self.labelFrameCasosPrueba, text='Operación: ')
      self.labelOperacionCasosPrueba.grid(column=0, row=0, padx=4, pady=4)
      self.datosOperacionCasosPrueba=tk.StringVar()
      operaciones=('Seleccione operación', 'AGREGAR', 'ACTUALIZAR', 'BORRAR')
      self.comboboxOperacionCasosPrueba=ttk.Combobox(self.labelFrameCasosPrueba, width=37, textvariable=self.datosOperacionCasosPrueba, values=operaciones, state='readonly')
      self.comboboxOperacionCasosPrueba.grid(column=1, row=0, padx=4, pady=0)
      self.comboboxOperacionCasosPrueba.current(0)

      self.labelCodigoCasosPrueba=ttk.Label(self.labelFrameCasosPrueba, text='Código: ')
      self.labelCodigoCasosPrueba.grid(column=0, row=1, padx=4, pady=4)
      self.datosCodigoCasosPrueba=tk.StringVar()
      self.entryCodigoCasosPrueba=ttk.Entry(self.labelFrameCasosPrueba, textvariable=self.datosCodigoCasosPrueba, width=40)
      self.entryCodigoCasosPrueba.grid(column=1, row=1, padx=4, pady=4)
      

      self.labelNombreCasosPrueba=ttk.Label(self.labelFrameCasosPrueba, text='Nombre:')
      self.labelNombreCasosPrueba.grid(column=0, row=2, padx=4, pady=4)
      self.datosNombreCasosPrueba=tk.StringVar()
      self.entryNombreCasosPrueba=ttk.Entry(self.labelFrameCasosPrueba, textvariable=self.datosNombreCasosPrueba, width=40)
      self.entryNombreCasosPrueba.grid(column=1, row=2, padx=4, pady=4)

      self.labelPrecioCasosPrueba=ttk.Label(self.labelFrameCasosPrueba, text='Precio:')
      self.labelPrecioCasosPrueba.grid(column=0, row=3, padx=4, pady=4)
      self.datosPrecioCasosPrueba=tk.StringVar()
      self.entryPrecioCasosPrueba=ttk.Entry(self.labelFrameCasosPrueba, textvariable=self.datosPrecioCasosPrueba, width=40)
      self.entryPrecioCasosPrueba.grid(column=1, row=3, padx=4, pady=4)

      self.labelInventarioCasosPrueba=ttk.Label(self.labelFrameCasosPrueba, text='Inventario:')
      self.labelInventarioCasosPrueba.grid(column=0, row=4, padx=4, pady=4)
      self.datosInventarioCasosPrueba=tk.StringVar()
      self.entryInventarioCasosPrueba=ttk.Entry(self.labelFrameCasosPrueba, textvariable=self.datosInventarioCasosPrueba, width=40)
      self.entryInventarioCasosPrueba.grid(column=1, row=4, padx=4, pady=4)

      self.botonProbar=ttk.Button(self.labelFrameCasosPrueba, text='Probar', command=self.probar, width=20)          # Pegar el boton en la pestaña, no el el 'LabelFrame'
      self.botonProbar.grid(column=2, row=2, padx=20, pady=4)


   def probar(self):
      pass
'''

# ---------- Bloque inicial ----------
app=Formulario()