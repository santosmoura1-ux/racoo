from sre_constants import CATEGORY_UNI_SPACE
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categoria/", views.categoria, name= "categoria" ),
    path("kit/", views.kit, name = "kit"),

]