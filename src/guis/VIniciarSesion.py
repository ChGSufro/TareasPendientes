import tkinter as tk
from rut_chile.rut_chile import format_capitalized_rut_without_dots as format_rut 
from src.guis.Gestor_de_campos import check_campos_inicio
from src.api.Api import log_usuario_event as log
from src.app.UsuarioActivo import UsuarioActivo
from src.guis.VPrincipal import VPrincipal
from src.guis.VBienvenida import VBienvenida

class VIniciarSesion(tk.Tk):
        """
        Clase encargada de la creación de la ventana de inicio de sesión, la cual se encarga de 
        recivir las credenciales ya existentes para una posterior validación y acceso al sistema.
        """
    
        def __init__(self):
    
            super().__init__()
            self.title("Iniciar Sesión")
    
            self.label = tk.Label(self, text='''
            Ingrese su nombre de usuario y contraseña.
            ''')
            self.label.pack(padx=20, pady=20)
    
            self.label_usuario = tk.Label(self, text="Usuario:")
            self.label_usuario.pack(pady=5)
            self.entry_usuario = tk.Entry(self)
            self.entry_usuario.pack(pady=5)
    
            self.label_contrasena = tk.Label(self, text="Contraseña:")
            self.label_contrasena.pack(pady=5)
            self.entry_contrasena = tk.Entry(self, show='*')
            self.entry_contrasena.pack(pady=5)

            self.resultado = tk.Label(self, text="")
            self.resultado.pack(pady=5)
    
            self.button_iniciar = tk.Button(self, text="Continuar", command=self.continuar)
            self.button_iniciar.pack(pady=10)

            self.button_regresar = tk.Button(self, text="Regresar", command=self.regresar)
            self.button_regresar.pack(pady=10)
    
            self.mainloop()

        def continuar(self):
            rut , contraseña = self.entry_usuario.get(), self.entry_contrasena.get()
            check = check_campos_inicio(rut, contraseña)
            if check[0]:
                respuesta = log({"Rut": format_rut(rut), "Contraseña": contraseña})["respuesta"]
                try:
                    usuario = UsuarioActivo(respuesta["Rut"], respuesta["Nombre"])
                    self.destroy()
                    VPrincipal(usuario)
                except TypeError:
                    self.resultado.config(text=respuesta)#por alguna razon no se actualiza el label
                    return      
            self.resultado.config(text=check[1])


        def regresar(self):
            """
            Metodo encargado de cerrar la ventana actual y regresar al usuario a la ventana 
            anterior en caso de que desee cancelar el inicio de sesión.
            """
            self.destroy()
            VBienvenida()

        
            