from rut_chile import rut_chile
#pip install rut-chilesour

# metodo que recibe un rut y verifica si es  valido, en caso de serlo retorna True, en caso contrario False.
#param rut: str -> rut a verificar
#return: bool -> True si es valido, False si no lo es
def check_rut(rut):
    try :
        return rut_chile.is_valid_rut(rut)
    except:
        return False

# metodo que recibe un campo y verifica si es nulo, en caso de serlo retorna False, en caso contrario True.
#param campo: str -> campo a verificar
#return: bool -> True si no es nulo, False si lo es
def check_noNull(campo):
    con = campo.replace(" ", "")
    if con == "":
        return False
    return True

# metodo que recibe una contraseña y una confirmacion de contraseña, verifica si son iguales, en caso de serlo retorna True, en caso contrario False.
#param contraseña: str -> contraseña a verificar
#param conf_contraseña: str -> confirmacion de contraseña
#return: bool -> True si son iguales, False si no lo son
def check_contraseña(contraseña, conf_contraseña):
    if contraseña != conf_contraseña:
        return False, "Las contraseñas no coinciden"
    return True, ""

# metodo que verifica si los campos rut y contraseña son minimamente validos para realizar una solicitud de inicio de sesion, retorna una tupla con un booleano y un mensaje.
#param rut: str -> rut a verificar
#param contraseña: str -> contraseña a verificar
#return: tuple -> (bool, str) -> (True, "") si los campos son validos, (False, mensaje) si no lo son
def check_campos_inicio(rut, contraseña):
    if not check_rut(rut):
        return False, "Usuario y/o contraseña incorrectos"
    if not check_noNull(contraseña):
        return False, "Usuario y/o contraseña incorrectos"
    return True, ""

# metodo que verifica si los campos rut, contraseña y confirmacion de contraseña son minimamente validos para realizar una solicitud de registro, retorna una tupla con un booleano y un mensaje.
#param rut: str -> rut a verificar
#param contraseña: str -> contraseña a verificar
def check_campos_registro(rut, contraseña, conf_contraseña):
    if not check_rut(rut):
        return False, "Rut invalido"
    if not check_noNull(contraseña):
        return False, "Ingrese una contraseña"
    if not check_contraseña(contraseña, conf_contraseña):
        return False, "Las contraseñas no coinciden"
    return True, ""

# metodo que verifica si elcampos nombre es minimamente valido para realizar una solicitud de creacion de tarea, retorna una tupla con un booleano y un mensaje.
#param nombre: str -> nombre a verificar
#return: tuple -> (bool, str) -> (True, "") si el campo es valido, (False, mensaje) si no lo es
def check_campos_nueva_tarea(nombre):
    if not check_noNull(nombre):
        return False, "Por favor ingrese un nombre"
    return True, ""

# metodo que verifica si el campo id_tarea es minimamente valido para realizar una solicitud de eliminacion de tarea, retorna una tupla con un booleano y un mensaje.
#param id_tarea: str -> id de la tarea a verificar
#return: tuple -> (bool, str) -> (True, "") si el campo es valido, (False, mensaje) si no lo es
def check_campos_seleccion_tarea(id_tarea):
    if not check_noNull(id_tarea):
        return False, "Por favor seleccione una tarea"
    if not id_tarea.isdigit():
        return False, "Por favor seleccione una tarea valida"
    return True, ""

    

    
