import firebase_admin 
from firebase_admin import credentials
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


try:
    firebase_admin.get_app()
except ValueError:
    cred = credentials.Certificate(os.path.join(BASE_DIR, 'static', 'greenlife-2023-firebase-adminsdk-tj7el-320309087c.json'))
    default_app = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://greenlife-2023-default-rtdb.firebaseio.com/',
    })

# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://greenlife-2023-default-rtdb.firebaseio.com/'
# })

