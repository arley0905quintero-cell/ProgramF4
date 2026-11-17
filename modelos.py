from excepciones import ClienteInvalidoError, ReservaInvalidaError
from servicios import Servicio

class Cliente:
    def __init__(self, id_cliente: str, nombre: str, correo: str):
        self._id_cliente = self._validar_id(id_cliente)
        self._nombre = self._validar_nombre(nombre)
        self._correo = self._validar_correo(correo)

    def _validar_id(self, id_cliente: str) -> str:
        if not id_cliente or not str(id_cliente).isalnum():
            raise ClienteInvalidoError(f"ID de cliente inválido: '{id_cliente}'. Debe ser alfanumérico.")
        return id_cliente

    def _validar_nombre(self, nombre: str) -> str:
        if not nombre or len(nombre.strip()) < 3:
            raise ClienteInvalidoError("El nombre del clente debe tener al menos 3 caracteres.") 
        return nombre.strip()

    def _validar_correo(self, correo: str) -> str:
        if "@" not in correo or "." not in correo:
            raise ClienteInvalidoError(f"Formato de correo electronico invalido: '{correo}'.")     
        return correo

    def __str__(self):
        return f"Cliente[{self._id_cliente}]: {self._nombre} ({self._correo})"

class Reserva:
    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio, duracion_horas: int):
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("se requiere un objeto Cliente valido.")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("se requiere un servicio valido.")
        if duracion_horas <= 0:
            raise ReservaInvalidaError("la duracion debe ser mayor a 0 horas.")

        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "PENDIENTE"
        self.costo_total = 0.0

    def procesar_reserva(self, descuento: float = 0.0):
        try:
            self.costo_total = self.servicio.calcular_costo(self.duracion_horas, descuento = descuento)
            self.estado = "CONFIRMADA"
        except Exception as e:
            self.estado = "RECHAZADA"
            raise ReservaInvalidaError(f"no se puede procesar la reserva: {e}") from e
        else:
            print(f"Reseerva {self.id_reserva} procesada con exito. Total: ${self.costo_total}")

        finally:
            print(f"Finalizado el intento de procesamiento para la reserva {self.id_reserva}.")

    def cancelar_reserva(self):
        if self.estado == "CANCELADA":
            raise ReservaInvalidaError("la reserva ya se encuentra cancelada.")
        self.estado = "CANCELADA"
        print(f"Reserva {self.id_reserva} cancelada exitosamente.")