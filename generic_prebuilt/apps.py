from django.apps import AppConfig


class GenericPrebuiltConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'generic_prebuilt'
