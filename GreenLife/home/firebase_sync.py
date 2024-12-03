from firebase_admin import db
from .firebase_config import default_app
from .models import (
    Counter, CounterDistancia, CounterHT, CounterLUX, CounterLluvia, CounterMQ7, CounterMQ8,
    CounterPH, CounterTC, CounterTDS, CounterTF, CounterTS
)

# Diccionario que mapea claves principales de Firebase a modelos de Django
MODELOS = {
    "Counter": Counter,
    "CounterDistancia": CounterDistancia,
    "CounterHT": CounterHT,
    "CounterLUX": CounterLUX,
    "CounterLluvia": CounterLluvia,
    "CounterMQ7": CounterMQ7,
    "CounterMQ8": CounterMQ8,
    "CounterPH": CounterPH,
    "CounterTC": CounterTC,
    "CounterTDS": CounterTDS,
    "CounterTF": CounterTF,
    "CounterTS": CounterTS,
}

# Diccionario que mapea las claves de los subcampos al nombre del campo en el modelo
CAMPOS_MODELOS = {
    "Counter": "cnt",
    "CounterDistancia": "cnt_distancia",
    "CounterHT": "cnt_ht",
    "CounterLUX": "cnt_lux",
    "CounterLluvia": "cnt_lluvia",
    "CounterMQ7": "cnt_mq7",
    "CounterMQ8": "cnt_mq8",
    "CounterPH": "cnt_ph",
    "CounterTC": "cnt_tc",
    "CounterTDS": "cnt_tds",
    "CounterTF": "cnt_tf",
    "CounterTS": "cnt_ts",
}

def sincronizar_datos_firebase():
    ref = db.reference('/')  # Conexión al nodo raíz de Firebase
    datos = ref.get()  # Obtener todos los datos

    if not datos:
        print("No se encontraron datos en Firebase.")
        return

    # Iterar por las claves principales en Firebase
    for key, value in datos.items():
        modelo = MODELOS.get(key)  # Obtener el modelo correspondiente
        campo = CAMPOS_MODELOS.get(key)  # Obtener el nombre del campo en el modelo

        if modelo and campo and isinstance(value, dict):
            for subkey, subvalue in value.items():
                # Asegúrate de manejar los subvalores correctamente
                try:
                    modelo.objects.update_or_create(
                        nodo=str(subkey),  # Convertir subkey a cadena
                        defaults={campo: subvalue.get(campo, 0)}  # Extraer el valor correspondiente
                    )
                    print(f"Sincronizado {key} -> {subkey}: {subvalue}")
                except Exception as e:
                    print(f"Error al sincronizar {key} -> {subkey}: {e}")
        else:
            print(f"Clave desconocida o datos no válidos: {key}")



# def sincronizar_datos_firebase():
#     ref = db.reference('/')  # Conexión al nodo raíz de Firebase
#     datos = ref.get()  # Obtener todos los datos

#     if not datos:
#         print("No se encontraron datos en Firebase.")
#         return

#     # Iterar por las claves principales en Firebase
#     for key, value in datos.items():
#         modelo = MODELOS.get(key)  # Obtener el modelo correspondiente
#         campo = CAMPOS_MODELOS.get(key)  # Obtener el nombre del campo en el modelo

#         if modelo and campo and isinstance(value, dict):
#             # Procesar los datos para el modelo correspondiente
#             for subkey, subvalue in value.items():
#                 # Actualizar o crear registros en el modelo correspondiente
#                 modelo.objects.update_or_create(
#                     id=str(subkey),  # Usar subkey como identificador único
#                     defaults={campo: subvalue}  # Asignar el valor al campo correspondiente
#                 )
#                 print(f"Sincronizado {key} -> {subkey}: {subvalue}")
#         else:
#             print(f"Clave desconocida o datos no válidos: {key}")