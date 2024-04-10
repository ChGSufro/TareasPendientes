import tkinter as tk
import json
from tkinter import ttk
from src.guis.VBienvenida import VBienvenida
from src.app.UsuarioActivo import UsuarioActivo
from src.guis.Gestor_de_campos import check_campos_nueva_tarea
from src.guis.Gestor_de_campos import check_campos_editar_tarea
from src.guis.Gestor_de_campos import check_campos_id


# Clase que representa la ventana principal de la aplicacion
# Esta ventana muestra las tareas del usuario activo en una tabla
# Permite al usuario cerrar sesion, agregar tareas, editar tareas y eliminar tareas
class VPrincipal(tk.Tk):
    
        def __init__(self, usuario: UsuarioActivo):

            self.usuario = usuario
    
            super().__init__()
            self.title("Gestor de tarea")

            self.menu = tk.Menu(self)
            self.menu.add_command(label="Cerrar Sesion", command=self.cerrar_sesion)
            
            self.config(menu=self.menu)

            self.label_bienvenida = tk.Label(self, text=f"Bienvenido: {self.usuario.getNombre()}")
            self.label_bienvenida.pack(pady=10)
    
            self.tabla = ttk.Treeview(self, columns=("Nombre", "Estado", "Descripcion"))
            self.tabla.heading("#0", text="Id")
            self.tabla.heading("#1", text="Nombre")
            self.tabla.heading("#2", text="Estado")
            self.tabla.heading("#3", text="Descripción")

            self.tabla.column("#0", width=50)
            self.tabla.column("#2", width=550)
            self.tabla.pack(pady=10)

            self.cargar_tabla()

            self.respuesta = tk.Label(self, text="")
            self.respuesta.pack(pady=10)

            self.ingresos = tk.Frame(self)
            self.ingresos.pack(pady=10)

            self.label_opcion = tk.Label(self.ingresos, text="Id:")
            self.label_opcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.Id = tk.Entry(self.ingresos)
            self.Id.pack(side=tk.LEFT, padx=10, pady=10)

            self.label_Nombre = tk.Label(self.ingresos, text="Nombre:")
            self.label_Nombre.pack(side=tk.LEFT, padx=10, pady=10)

            self.Nombre = tk.Entry(self.ingresos)
            self.Nombre.pack(side=tk.LEFT, padx=10, pady=10)

            self.label_Descripcion = tk.Label(self.ingresos, text="Descripcion:")
            self.label_Descripcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.Descripcion = tk.Entry(self.ingresos)
            self.Descripcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.label_Estado = tk.Label(self.ingresos, text="Estado:")
            self.label_Estado.pack(side=tk.LEFT, padx=10, pady=10)

            self.Estado = ttk.Combobox(self.ingresos, values=["Pendiente", "En Proceso", "Finalizada"])
            self.Estado.pack(side=tk.LEFT, padx=10, pady=10)    

            self.espacio = tk.Label(self, text="")
            self.espacio.pack(side=tk.LEFT, padx=130, pady=30)

            self.button_agregar_tarea = tk.Button(self, text="Agregar Tarea", command=self.agregar_tarea)
            self.button_agregar_tarea.pack(side=tk.LEFT, padx=30, pady=5)

            self.button_editar_tarea = tk.Button(self, text="Editar Tarea", command=self.editar_tarea)
            self.button_editar_tarea.pack(side=tk.LEFT, padx=30, pady=5)

            self.button_eliminar_tarea = tk.Button(self, text="Eliminar Tarea", command=self.eliminar_tarea)
            self.button_eliminar_tarea.pack(side=tk.LEFT, padx=30, pady=5)
            
            self.mainloop()

    # Metodo que actualiza la tabla de tareas
        def cargar_tabla(self):
            for dato in self.tabla.get_children():
                self.tabla.delete(dato)
            for tarea in self.usuario.getTareas():
                self.tabla.insert("", "end", text=tarea.getId(), values=(tarea.getNombre(), tarea.getDescripcion(), tarea.getEstado()))
    
    # Metodo que cierra la sesion del usuario activo y nos regresa a la ventana de bienvenida
        def cerrar_sesion(self):
            self.destroy()
            VBienvenida()

    # Metodo que nos lleva a la ventana de agregar tarea
        def agregar_tarea(self):
            nombre = self.Nombre.get()
            descripcion = self.Descripcion.get()
            ok = check_campos_nueva_tarea(nombre, descripcion)
            if ok[0]:
                self.respuesta.config(text=self.usuario.agregar_tarea(nombre, descripcion))
                self.usuario.cargar_tareas()
                self.cargar_tabla()
                return
            self.respuesta.config(text=ok[1])


    # Metodo que nos lleva a la ventana de editar tarea
        def editar_tarea(self):
            id = self.Id.get()
            nombre = self.Nombre.get()
            descripcion = self.Descripcion.get()
            estado = self.Estado.get()
            try:
                ok = check_campos_editar_tarea(id)
                if ok:
                    self.respuesta.config(text=self.usuario.editar_tarea(id, nombre, descripcion, estado))
                    self.usuario.cargar_tareas()
                    self.cargar_tabla()
                    return
            except ValueError as error:
                self.respuesta.config(text=str(error))
                return
            self.respuesta.config(text="Por favor ingrese un nombre, descripcion o estado.")


    # Metodo que elimina una tarea o muestra un mensaje de error si no se puede eliminar
        def eliminar_tarea(self):
            id = self.Id.get()
            ok = check_campos_id(id)
            if ok[0]:
                self.respuesta.config(text=self.usuario.eliminar_tarea(id))
                self.usuario.cargar_tareas()
                self.cargar_tabla()
                return
            self.respuesta.config(text=ok[1])
            
                

    
            