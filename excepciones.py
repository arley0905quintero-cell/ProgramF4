class SoftwareFJError(Exception):
    "Excepcion base para todas las excepciones personalizadas de Software FJ."
    pass

class ClienteInvalidoError(SoftwareFJError):
    "se lanza cuando los datos del cliente (ID, nombre o correo) no cumplen con las validaciones."
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    "se lanza cuando un servicio no esta disponible, la tarifa es invalida o los parametros son incorrectos"
    pass

class ReservaInvalidaError(SoftwareFJError):
    "se lanza cuando ocurre un fallo al intentar procesar o cancelar una reserva."
    pass