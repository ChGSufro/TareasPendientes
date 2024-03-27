import tkinter as tk
from src.guis.VBienvenida import VBienvenida
from src.guis.Gestor_de_campos import check_campos_registro
from src.api.Api import post_usuarios_event as agregar_usuario
from rut_chile.rut_chile import format_capitalized_rut_without_dots as format_rut

class VRegistro(tk.Tk):
    #Clase encargada de la creación de la ventana de registro, la cual se encarga de recibir los datos necesarios para la creación de un nuevo usuario.
    
    def __init__(self):
    
        super().__init__()
        self.title("Registro")
    
        self.label = tk.Label(self, text='''
        Ingrese su nombre de usuario y contraseña.
        ''')
        self.label.pack(padx=20, pady=20)
    
        self.label_usuario = tk.Label(self, text="Rut::")
        self.label_usuario.pack(pady=5)
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack(pady=5)

        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack(pady=5)
    
        self.label_contrasena = tk.Label(self, text="Contraseña:")
        self.label_contrasena.pack(pady=5)
        self.entry_contrasena = tk.Entry(self, show='*')
        self.entry_contrasena.pack(pady=5)

        self.label_confirmar_contrasena = tk.Label(self, text="Confirmar Contraseña:")
        self.label_confirmar_contrasena.pack(pady=5)
        self.entry_confirmar_contrasena = tk.Entry(self, show='*')
        self.entry_confirmar_contrasena.pack(pady=5)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.pack(pady=5)
    
        self.button_registrar = tk.Button(self, text="Registrar", command=self.registrar)
        self.button_registrar.pack(pady=10)

        self.button_regresar = tk.Button(self, text="Regresar", command=self.regresar)
        self.button_regresar.pack(pady=10)
    
        self.mainloop()

    #Metodo encargado de verificar si los campos ingresados son validos y en caso de serlo, realiza la solicitud de registro.   
    def registrar(self):
        rut, nombre, contraseña, confcontraseña = self.entry_usuario.get(), self.entry_nombre.get(), self.entry_contrasena.get(), self.entry_confirmar_contrasena.get()
        check = check_campos_registro(rut, contraseña, confcontraseña)
        if check[0]:
            respuesta = agregar_usuario({"Rut": format_rut(rut), "Nombre": nombre, "Contraseña": contraseña})["respuesta"]
            try:
                self.label_resultado.config(text=respuesta)
                self.limpiar()
                return
            except TypeError:
                self.label_resultado.config(text=respuesta)
                return
        self.label_resultado.config(text=check[1])
            
    #Metodo encargado de cerrar la ventana actual y regresar al usuario a la ventana anterior en caso de que desee cancelar el registro.
    def regresar(self):
        self.destroy()
        VBienvenida()

    #Metodo encargado de limpiar los campos de la ventana.
    def limpiar(self):
        self.entry_usuario.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_contrasena.delete(0, tk.END)
        self.entry_confirmar_contrasena.delete(0, tk.END)