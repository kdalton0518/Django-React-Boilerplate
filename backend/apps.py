from django.apps import AppConfig


class BackendConfig(AppConfig):
    name = "backend"
    verbose_name = "Public website"
    default_auto_field = 'django.db.models.BigAutoField'


    def ready(self):
        return
