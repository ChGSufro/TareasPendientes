import tkinter as tk


class VBienvenida(tk.Tk):
    """
    Clase encargada de la creación de la ventana de bienvenida, la cual es la primera ventana 
    que se muestra al usuario y despliega las opciones de iniciar sesión o registrar un usuario nuevo. 
    """

    def __init__(self):

        super().__init__()
        self.title("Bienvenido")

        self.label = tk.Label(self, text="Bienvenido al administrador de tareas.\n\nPor favor, seleccione una opción del menú.")
        self.label.pack(padx=20, pady=20)

        self.button_iniciar = tk.Button(self, text="Iniciar Sesión", command=self.iniciar)
        self.button_iniciar.pack(pady=10)

        self.button_registrar = tk.Button(self, text="Registrar", command=self.registrar)
        self.button_registrar.pack(pady=10)

        self.mainloop()


    def iniciar(self):
        """
        Metodo encargado de cerrae la ventana actual y abrir la ventana de inicio de 
        sesion una vez clickeado el botón .
        """
        self.destroy()
        from src.guis.VIniciarSesion import VIniciarSesion
        VIniciarSesion()
        
    def registrar(self):
        """
        Metodo encargado de cerrar la ventana actual y abrir la ventana de registro una 
        vez clickeado el botón.
        """
        self.destroy()
        from src.guis.VRegistro import VRegistro
        VRegistro()
        