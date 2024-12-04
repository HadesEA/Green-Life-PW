from firebase_admin import db
from .firebase_config import *
from .models import (
    Counter, CounterDistancia, CounterHT, CounterLUX, CounterLluvia,
    CounterMQ7, CounterMQ8, CounterPH, CounterTC, CounterTDS, CounterTF, CounterTS
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
    "Counter": {"campo_valor": "cnt", "campo_nodo": "node"},
    "CounterDistancia": {"campo_valor": "cntDistancia", "campo_nodo": "nodeDistancia"},
    "CounterHT": {"campo_valor": "cntHT", "campo_nodo": "nodeHT"},
    "CounterLUX": {"campo_valor": "cntLUX", "campo_nodo": "nodeLUX"},
    "CounterLluvia": {"campo_valor": "cntLluvia", "campo_nodo": "nodeLluvia"},
    "CounterMQ7": {"campo_valor": "cntMQ7", "campo_nodo": "nodeMQ7"},
    "CounterMQ8": {"campo_valor": "cntMQ8", "campo_nodo": "nodeMQ8"},
    "CounterPH": {"campo_valor": "cntPH", "campo_nodo": "nodePH"},
    "CounterTC": {"campo_valor": "cntTC", "campo_nodo": "nodeTC"},
    "CounterTDS": {"campo_valor": "cntTDS", "campo_nodo": "nodeTDS"},
    "CounterTF": {"campo_valor": "cntTF", "campo_nodo": "nodeTF"},
    "CounterTS": {"campo_valor": "cntTS", "campo_nodo": "nodeTS"},
}

def sincronizar_datos_firebase():
    ref = db.reference('/')
    datos = ref.get()

    if not datos:
        print("No se encontraron datos en Firebase.")
        return

    for key, value in datos.items():
        modelo = MODELOS.get(key)
        config = CAMPOS_MODELOS.get(key)

        if modelo and config and isinstance(value, dict):
            campo_valor = config["campo_valor"]
            campo_nodo = config["campo_nodo"]

            for subkey, subvalue in value.items():
                nodo = subvalue.get(campo_nodo, subkey)
                valor = subvalue.get(campo_valor, 0)

                # Depuración para CounterHT
                if key == "CounterHT":
                    print(f"Depurando CounterHT: nodo={nodo}, valor={valor}")

                # Depuración general: Imprime todos los datos que intentas guardar
                print(f"Sincronizando tabla {key}: nodo={nodo}, valor={valor}")

                # Actualiza o crea registros
                modelo.objects.update_or_create(
                    nodo=str(nodo),
                    defaults={campo_valor: valor}
                )
        else:
            print(f"Clave desconocida o datos no válidos: {key}")
