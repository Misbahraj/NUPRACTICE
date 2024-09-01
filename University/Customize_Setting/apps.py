from django.apps import AppConfig


class CustomizeSettingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Customize_Setting'
