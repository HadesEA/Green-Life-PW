from django.apps import AppConfig
import threading
import sys

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        # No iniciar sincronización durante migraciones
        if 'migrate' in sys.argv or 'makemigrations' in sys.argv:
            return

        from .firebase_sync import sincronizar_datos_firebase
        threading.Thread(target=sincronizar_datos_firebase).start()
