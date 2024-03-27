import tkinter as tk
from tkinter import ttk
from src.guis.VBienvenida import VBienvenida
from src.app.UsuarioActivo import UsuarioActivo
from src.api.Api import delete_tareas_event as eliminar
from src.api.Api import put_tareas_event as editar

class VPrincipal(tk.Tk):
    
        def __init__(self, usuario: UsuarioActivo):

            self.usuario = usuario
    
            super().__init__()
            self.title("Bienvenido")

            self.button_cerrar_sesion = tk.Button(self, text="Cerrar Sesion", command=self.cerrar_sesion)
            self.button_cerrar_sesion.pack(pady=10)

            self.label_bienvenida = tk.Label(self, text=f"Bienvenido {self.usuario.getNombre()}")
            self.label_bienvenida.pack(pady=10)

            self.button_agregar_tarea = tk.Button(self, text="Agregar Tarea", command=self.destroy)
            self.button_agregar_tarea.pack(pady=10)
    
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

            self.espacio = tk.Label(self, text="")
            self.espacio.pack(side=tk.LEFT, padx=75)


            self.label_opcion = tk.Label(self, text="Ingrese el id:")
            self.label_opcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.opcion = tk.Entry(self)
            self.opcion.pack(side=tk.LEFT, padx=10, pady=10)

            self.button_editar_tarea = tk.Button(self, text="Editar Tarea", command=self.destroy)
            self.button_editar_tarea.pack(side=tk.LEFT)

            self.button_eliminar_tarea = tk.Button(self, text="Eliminar Tarea", command=self.eliminar_tarea)
            self.button_eliminar_tarea.pack(side=tk.LEFT)
            
            self.mainloop()
    
        def cerrar_sesion(self):
            self.destroy()
            VBienvenida()

        def eliminar_tarea(self):
            pass

        def eliminar_tarea(self, id):
            pass