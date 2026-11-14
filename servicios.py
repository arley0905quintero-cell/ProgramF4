from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError

class Servicio(ABC):
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float):
        if tarifa_base <= 0:
            raise ServicioNoDisponibleError("La tarifa base debe ser mayor a cero.")
        self._id_servicio = id_servicio
        self._nombre = nombre
        self._tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, horas: int, descuento: float = 0.0, impuesto: float = 0.19) -> float:
        "Metodo abstracto pr calcular costos con parametros opcionales."
        pass


    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass


class ReservaSala(Servicio):
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, capacidad: int):
            super().__init__(id_servicio, nombre, tarifa_base)
            self.capacidad = capacidad

    def calcular_costo(self, horas: int, descuento: float = 0.0, impuesto: float = 0.19) -> float:
         if horas <= 0:
              raise ServicioNoDisponibleError("la duracion debe ser al menos de 1 hora")
         subtotal = (self._tarifa_base * horas) * (1 - descuento)
         return round(subtotal * (1 + impuesto), 2)

    def obtener_descripcion(self) -> str:
         return f"Reserva de sala: {self._nombre} (capacidad: {self.capacidad} personas)"


class AlquilerEquipo(Servicio): 
     def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, deposito: float):
             super().__init__(id_servicio, nombre, tarifa_base)
             self.deposito = deposito

     def calcular_costo(self, horas: int, descuento: float = 0.0, impuesto: float = 0.19) -> float:
          if horas <= 0:
               raise ServicioNoDisponibleError("las horas de alquiler deben ser mayores a 0.")
          subtotal = (self._tarifa_base * horas) * (1 - descuento)
          return round((subtotal * (1 + impuesto)) + self.deposito, 2)

     def obtener_descripcion(self) -> str:
          return f"Alquiler de Equipo: {self._nombre} (Deposito: ${self.deposito})"


class AsesoriaExpecializada(Servicio):
        def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, especialista: str ):
             super().__init__(id_servicio, nombre, tarifa_base)
             self.especialista = especialista

        def calcular_costo(self, horas: int, descuento: float = 0.0, impuesto: float = 0.19) -> float:
             if horas < 2:
                  raise ServicioNoDisponibleError("las asesorias especializadas requieren un minimo de 2 horas.")
             subtotal = (self._tarifa_base * horas) * (1 - descuento)
             return round(subtotal * (1 + impuesto), 2)

        def obtener_descripcion(self) -> str:
             return f"Asesoria Especializada con el experto {self.especialista}"
             
             
                   
          
          
                  




    
         
                 