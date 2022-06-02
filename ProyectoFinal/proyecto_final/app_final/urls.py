from django.urls import path
from app_final import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('registrar_usuario', views.registrar_usuario, name="Registrar Usuario"),
    path('agregar_juego', views.agregar_juego, name="Agregar Juego"),
    path('crear_review', views.crear_review, name="Crear Review"),
    path('ver_todo', views.ver_todo, name="Ver Reviews" ),
    path('ver_por_juego', views.ver_por_juego, name="Filtrar Reviews"),
    path('ver_por_usuario', views.ver_por_usuario, name="Filtrar Usuarios"),
    path('ver_por_juego_resultado', views.ver_por_juego_resultado),
    path('ver_por_usuario_resultado', views.ver_por_usuario_resultado),
]