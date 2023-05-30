from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shop"



class UsersConfig(AppConfig):
    name = 'profile'

    def ready(self):
        import shop.signals