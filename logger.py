import logging

#configuracion del log en archivo plano
logging.basicConfig(
    filename="sistema_software_fj.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)

def registrar_log(nivel, mensaje):
    if nivel.lower() == "info":
        logging.info(mensaje)
    elif nivel.lower() == "error":
        logging.error(mensaje)
    elif nivel.lower() == "warning":
        logging.warning(mensaje)        