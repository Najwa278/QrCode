'''from django.apps import AppConfig


class QrcodesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qr_maker'
'''
from django.apps import AppConfig

class QrMakerConfig(AppConfig):  # Match the class name with the app's purpose
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qr_maker'  # Match this to your folder name
