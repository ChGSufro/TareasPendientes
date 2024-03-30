import tkinter as tk
import json
from tkinter import ttk
from src.guis.VBienvenida import VBienvenida
from src.guis.Gestor_de_campos import check_campos_seleccion_tarea as check
from src.guis.Gestor_de_campos import check_campos_nueva_tarea as check_nueva_tarea
from src.guis.Gestor_de_campos import check_campos_editar_tarea as check_editar_tarea
from src.app.UsuarioActivo import UsuarioActivo
from src.api.Api import delete_tareas_event as eliminar
from src.api.Api import post_tareas_event as agregar
from src.api.Api import put_tareas_event as editar

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
    
            self.tabla = ttk.Treeview(self, columns=("Nombre", "Descripcion", "Estado"))
            self.tabla.heading("#0", text="Id")
            self.tabla.heading("#1", text="Nombre")
            self.tabla.heading("#2", text="Descripcion")
            self.tabla.heading("#3", text="Estado")

            self.tabla.column("#0", width=50)
            self.tabla.column("#2", width=400)

            self.tabla.pack(pady=10)

            for tarea in usuario.getTareas():
                self.tabla.insert("", "end", text=tarea.getId(), values=(tarea.getNombre(), tarea.getDescripcion(), tarea.getEstado()))

            self.respuesta = tk.Label(self, text="aaa")
            self.respuesta.pack(pady=10)

            self.label_opcion = tk.Label(self, text="Id:")
            self.label_opcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.opcion = tk.Entry(self)
            self.opcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.label_Nombre = tk.Label(self, text="Nombre:")
            self.label_Nombre.pack(side=tk.LEFT, padx=10, pady=10)

            self.Nombre = tk.Entry(self)
            self.Nombre.pack(side=tk.LEFT, padx=10, pady=10)

            self.label_Descripcion = tk.Label(self, text="Descripcion:")
            self.label_Descripcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.Descripcion = tk.Entry(self)
            self.Descripcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.label_Estado = tk.Label(self, text="Estado:")
            self.label_Estado.pack(side=tk.LEFT, padx=10, pady=10)

            self.Estado = tk.Entry(self)
            self.Estado.pack(side=tk.LEFT, padx=10, pady=10)    

            self.button_agregar_tarea = tk.Button(self, text="Agregar Tarea", command=self.agregar_tarea)
            self.button_agregar_tarea.pack(padx=30, pady=5)

            self.button_editar_tarea = tk.Button(self, text="Editar Tarea", command=self.editar_tarea)
            self.button_editar_tarea.pack(padx=30, pady=5)

            self.button_eliminar_tarea = tk.Button(self, text="Eliminar Tarea", command=self.eliminar_tarea)
            self.button_eliminar_tarea.pack(padx=30, pady=5)
            
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
            Nombre = self.Nombre.get()
            Descripcion = self.Descripcion.get()
            CH_G_check = check_nueva_tarea(Nombre)
            if CH_G_check[0]:
                CH_G_tarea= {"Usuario": self.usuario.getRut(), "Nombre": Nombre, "Descripcion": Descripcion, "Estado": "Pendiente"}
                CH_G_respuesta = agregar(CH_G_tarea)["respuesta"]
                self.respuesta.config(text=CH_G_respuesta)
                self.usuario.updateTareas()
                self.cargar_tabla()
                return
            self.respuesta.config(text=CH_G_check[1])

    # Metodo que nos lleva a la ventana de editar tarea
        def editar_tarea(self):
            pass


    # Metodo que elimina una tarea o muestra un mensaje de error si no se puede eliminar
        def eliminar_tarea(self):
            id = self.opcion.get()
            check_con = check(id)
            if not check_con[0] and not self.usuario.mi_tarea_existe(int(id)):
                self.respuesta.config(text=check_con[1])
                return
            respuesta = eliminar(int(id))["respuesta"]
            if respuesta != "Tarea eliminada.":
                self.respuesta.config(text=respuesta)
                return
            self.usuario.updateTareas()
            self.cargar_tabla()
                

    
            