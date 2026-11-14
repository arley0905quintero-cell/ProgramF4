from modelos import Cliente, Reserva
from servicios import ReservaSala, AlquilerEquipo, AsesoriaExpecializada
from excepciones import SoftwareFJError
from logger import registrar_log

def ejecutar_operacion(numero_op, funcion):
    print(f"\n--- OPERACION #{numero_op} ---")
    try:
        resultado = funcion()
        registrar_log("INFO", f"operacion #{numero_op} exitosa: {resultado}")
    except SoftwareFJError as e:
        registrar_log("ERROR", f"operacion #{numero_op} fallo por excepcion de negocio: {e}")
        print(f"[ERROR CAPTURADO]: {e}")
    except Exception as e:
        registrar_log("ERROR", f"operacion #{numero_op} fallo por error inesperado: {e}")
        print(f"[ERROR INESPERADO]: {e}")
    else:
        print(f"operacion #{numero_op} completada sin inconvenientes.")
    finally:
        print(f"fin de la ejecucion de la operacion #{numero_op}.")



def main():
    print("=== INICIANDO SISTEMA INTEGRAL SOFTWARE FJ ===")

    #1. CLIENTE VALIDO
    c1 = None
    def op1():
        nonlocal c1
        c1 = Cliente("C01", "Carlos Mendoza", "carlos@gmail.com")
        return f"Cliente creado: {c1}"
    ejecutar_operacion(1, op1)

    #2 cliente invalido (correo incorrecto sin @ ni .com)
    def op2():
        return Cliente("C02", "Ana Gomez", "correo_invalido_sin_arroba")
    ejecutar_operacion(2, op2)

    #3. creacion de servicio valido (sala de juntas)
    s1 = None
    def op3():
        nonlocal s1
        s1 = ReservaSala("S01", "Sala A", 50000, 10)
        return f"Servicio creado: {s1.obtener_descripcion()}"
    ejecutar_operacion(3, op3)

    #4. creacion de servicio invalido (tarifa base negativa)
    def op4():
        return AlquilerEquipo("E01", "proyector 4K", -15000, 50000)
    ejecutar_operacion(4, op4)

    #5. reserva valida
    r1 = None
    def op5():
        nonlocal r1
        r1 = Reserva("R01", c1, s1, 3)
        r1.procesar_reserva(descuento=0.10)
        return f"reserva {r1.id_reserva} confirmada."
    ejecutar_operacion(5, op5)

    #6. reserva invalida (duracion de asesoria menor a 2 horas)
    def op6():
        s_asesoria = AsesoriaExpecializada("A01", "Arquitectura Cloud", 80000, "Ing. Perez")
        r_invalid = Reserva("R02", c1, s_asesoria, 1) #requiere minimo 2 horas
        r_invalid.procesar_reserva()
        return "Reserva procesada."
    ejecutar_operacion(6, op6)

    #7. creacion de alquiler de equipo valido
    e1 = None
    def op7():
        nonlocal e1
        e1 = AlquilerEquipo("E02", "Servidor Portatil", 120000, 300000)
        return f"Equipo creado: {e1.obtener_descripcion()}"
    ejecutar_operacion(7, op7)

    #8. reserva de equipo valido con descuento
    def op8():
        r3 = Reserva("R03", c1, e1, 5)
        r3.procesar_reserva(descuento=0.15)
        return f"Reserva {r3.id_reserva} exitosa."
    ejecutar_operacion(8, op8)

    #9. cancelacion de reserva valida
    def op9():
        r1.cancelar_reserva()
        return f"Reserva {r1.id_reserva} cancelada."
    ejecutar_operacion(9, op9)

    #10. Re-cancelacion Invalida (lanza excepcion por que ya esta cancelada)
    def op10():
        r1.cancelar_reserva()
        return "Cancelacion procesada."
    ejecutar_operacion(10, op10)

    print("\n=== EJECUCION FINALIZADA EXITOSAMENTE (revisar sistema_software_fj.log) ===")


if __name__ == "__main__":
    main()
    

