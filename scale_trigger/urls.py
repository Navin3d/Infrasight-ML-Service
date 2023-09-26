from django.urls import path
from . import views
urlpatterns=[
    path("scale_trigger/<int:cpu>/<int:disk>/<int:ram>/<int:load>/<int:uptime>/",views.scale_decision)
]