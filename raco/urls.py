from sre_constants import CATEGORY_UNI_SPACE
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre" ),
    path("kit/", views.kit, name ="kit"),
    path("convite/", views.convite, name ="convite"),
    path("lembranca/", views.lembranca, name ="lembranca"),

]