from django.apps import AppConfig


class KartConfig(AppConfig):
    name = 'kart'

    def ready(self):
        from . import signals
