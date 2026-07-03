from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('consultas/', views.lista_consultas, name='lista_consultas'),
    path('consulta/nueva/', views.crear_consulta, name='crear_consulta'),
    path('consulta/<int:pk>/', views.detalle_consulta, name='detalle_consulta'),
    path('consulta/<int:pk>/editar/', views.editar_consulta, name='editar_consulta'),
    path('consulta/<int:pk>/eliminar/', views.eliminar_consulta, name='eliminar_consulta'),
]