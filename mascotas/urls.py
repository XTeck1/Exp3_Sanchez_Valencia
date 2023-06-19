from django.urls import path
from .views import index, mision, productos, voluntariado, listaVoluntarios, registroStock, ingresarProducto, modificarProducto, eliminarProducto

urlpatterns=[
    path('', index, name="index"),
    path('mision/', mision, name="mision"),
    path('productos/', productos, name="productos"),
    path('voluntariado/', voluntariado, name="voluntariado"),
    path('listaVoluntarios/', listaVoluntarios, name="listaVoluntarios"),
    path('registroStock/', registroStock, name="registroStock"),
    path('ingresarProducto/', ingresarProducto, name="ingresarProducto"),
    path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
]