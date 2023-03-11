from django.apps import AppConfig

#註冊的名稱 到settings.py寫 INSTALLED_APPS 'app01.apps.App01Config'
class App01Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app01'
