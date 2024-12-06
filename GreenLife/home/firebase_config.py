import firebase_admin
from firebase_admin import credentials
import os

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Inicialización de Firebase
try:
    # Verifica si ya existe una instancia inicializada
    firebase_admin.get_app()
except ValueError:
    # Inicializa la app con las credenciales y la URL de la base de datos
    cred = credentials.Certificate(os.path.join(BASE_DIR, 'static', 'greenlife-2023-firebase-adminsdk-tj7el-a2b290fbce.json'))
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://greenlife-2023-default-rtdb.firebaseio.com/'
    })
