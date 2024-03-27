from rut_chile import rut_chile
#pip install rut-chilesour

# metodo que recibe un rut y verifica si es  valido, en caso de serlo retorna True, en caso contrario False.
def check_rut(rut):
    try :
        return rut_chile.is_valid_rut(rut)
    except:
        return False

# metodo que recibe una contraseña y verifica si no esta vacia, en caso de serlo retorna True, en caso contrario False.
def check_noNull(contraseña):
    con = contraseña.replace(" ", "")
    if con == "":
        return False
    return True

# metodo que recibe una contraseña y una confirmacion de contraseña, verifica si son iguales, en caso de serlo retorna True, en caso contrario False.
def check_contraseña(contraseña, conf_contraseña):
    if contraseña != conf_contraseña:
        return False, "Las contraseñas no coinciden"
    return True, ""

# metodo que verifica si los campos rut y contraseña son minimamente validos para realizar una solicitud de inicio de sesion, retorna una tupla con un booleano y un mensaje.
def check_campos_inicio(rut, contraseña):
    if not check_rut(rut):
        return False, "Usuario y/o contraseña incorrectos"
    if not check_noNull(contraseña):
        return False, "Usuario y/o contraseña incorrectos"
    return True, ""

# metodo que verifica si los campos rut, contraseña y confirmacion de contraseña son minimamente validos para realizar una solicitud de registro, retorna una tupla con un booleano y un mensaje.
def check_campos_registro(rut, contraseña, conf_contraseña):
    if not check_rut(rut):
        return False, "Rut invalido"
    if not check_noNull(contraseña):
        return False, "Ingrese una contraseña"
    if not check_contraseña(contraseña, conf_contraseña):
        return False, "Las contraseñas no coinciden"
    return True, ""

# metodo que verifica si elcampos nombre es minimamente valido para realizar una solicitud de creacion de tarea, retorna una tupla con un booleano y un mensaje.
def check_campos_nueva_tarea(nombre):
    if not check_noNull(nombre):
        return False, "Por favor ingrese un nombre"
    return True, ""

# metodo que verifica si el campo id_tarea es minimamente valido para realizar una solicitud de eliminacion de tarea, retorna una tupla con un booleano y un mensaje.
def check_campos_seleccion_tarea(id_tarea):
    if not check_noNull(id_tarea):
        return False, "Por favor seleccione una tarea"
    if not id_tarea.isdigit():
        return False, "Por favor seleccione una tarea valida"
    return True, ""

    

    
