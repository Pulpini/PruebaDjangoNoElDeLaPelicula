from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# ==============================
# Django REST Framework
# ==============================

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    RegistroSerializer,
    ArticuloSerializer,
)
# Importamos el modelo Articulo
from .models import Articulo

# Importamos el formulario basado en el modelo
from .forms import ArticuloForm


# ==========================================================
# LISTAR ARTÍCULOS
# ==========================================================
#
# Esta vista corresponde a la operación READ del CRUD.
#
# Función:
# - Si el usuario NO ha iniciado sesión:
#       solamente verá los artículos publicados.
#
# - Si el usuario inició sesión:
#       verá todos los artículos creados por él,
#       incluso aquellos que aún no están publicados.
#
# Parámetros:
# request -> petición HTTP enviada por el navegador.
#
# Retorna:
# Template lista.html junto con la lista de artículos.
# ==========================================================
def lista_articulos(request):

    if request.user.is_authenticated:

        articulos = Articulo.objects.filter(
            autor=request.user
        )

    else:

        articulos = Articulo.objects.filter(
            publicado=True
        )

    return render(
        request,
        "blog/lista.html",
        {
            "articulos": articulos
        }
    )


# ==========================================================
# DETALLE DEL ARTÍCULO
# ==========================================================
#
# Muestra toda la información de un artículo.
#
# get_object_or_404():
# Busca un objeto por su ID.
#
# Si no existe genera automáticamente un error 404.
#
# Además verifica que un usuario no pueda acceder
# a artículos privados pertenecientes a otro autor.
# ==========================================================
def detalle_articulo(request, pk):

    articulo = get_object_or_404(
        Articulo,
        pk=pk
    )

    # Si el artículo no está publicado y además
    # el usuario no es su autor, se bloquea el acceso.
    if (
        not articulo.publicado
        and articulo.autor != request.user
    ):

        messages.error(
            request,
            "Este artículo no está disponible."
        )

        return redirect(
            "lista_articulos"
        )

    return render(
        request,
        "blog/detalle.html",
        {
            "articulo": articulo
        }
    )


# ==========================================================
# CREAR ARTÍCULO
# ==========================================================
#
# Corresponde a la operación CREATE del CRUD.
#
# Solo usuarios autenticados pueden crear artículos.
#
# GET
# ----
# Muestra el formulario vacío.
#
# POST
# -----
# Recibe los datos ingresados por el usuario.
#
# commit=False
# -------------
# Permite modificar el objeto antes de guardarlo
# en la base de datos.
#
# En este caso se asigna automáticamente
# el usuario autenticado como autor.
# ==========================================================
@login_required
def crear_articulo(request):

    if request.method == "POST":

        form = ArticuloForm(request.POST)

        if form.is_valid():

            # No guardar todavía.
            articulo = form.save(commit=False)

            # Asignar automáticamente el usuario.
            articulo.autor = request.user

            # Guardar finalmente en SQLite.
            articulo.save()

            messages.success(
                request,
                "¡Artículo creado exitosamente!"
            )

            return redirect(
                "detalle_articulo",
                pk=articulo.pk
            )

    else:

        form = ArticuloForm()

    return render(
        request,
        "blog/form.html",
        {
            "form": form,
            "accion": "Crear"
        }
    )


# ==========================================================
# EDITAR ARTÍCULO
# ==========================================================
#
# Corresponde a UPDATE del CRUD.
#
# Solo el propietario puede modificar
# sus propios artículos.
#
# instance=articulo
# -----------------
# Indica que el formulario trabajará sobre
# un registro existente y no creará uno nuevo.
# ==========================================================
@login_required
def editar_articulo(request, pk):

    articulo = get_object_or_404(
        Articulo,
        pk=pk,
        autor=request.user
    )

    if request.method == "POST":

        form = ArticuloForm(
            request.POST,
            instance=articulo
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "¡Artículo actualizado correctamente!"
            )

            return redirect(
                "detalle_articulo",
                pk=articulo.pk
            )

    else:

        form = ArticuloForm(
            instance=articulo
        )

    return render(
        request,
        "blog/form.html",
        {
            "form": form,
            "accion": "Editar",
            "articulo": articulo
        }
    )


# ==========================================================
# ELIMINAR ARTÍCULO
# ==========================================================
#
# Corresponde a DELETE del CRUD.
#
# Solamente el autor del artículo
# tiene permiso para eliminarlo.
#
# Primero muestra una página de confirmación.
#
# Si el usuario confirma (POST),
# el registro se elimina de SQLite.
# ==========================================================
@login_required
def eliminar_articulo(request, pk):

    articulo = get_object_or_404(
        Articulo,
        pk=pk,
        autor=request.user
    )

    if request.method == "POST":

        articulo.delete()

        messages.success(
            request,
            "Artículo eliminado correctamente."
        )

        return redirect(
            "lista_articulos"
        )

    return render(
        request,
        "blog/confirmar_eliminar.html",
        {
            "articulo": articulo
        }
    )
# ==========================================================
# API PÚBLICA
# ==========================================================

@api_view(["GET"])
@permission_classes([AllowAny])
def api_publica(request):

    return Response({
        "mensaje": "Esta es una ruta pública."
    })


# ==========================================================
# REGISTRO
# ==========================================================

@api_view(["POST"])
@permission_classes([AllowAny])
def registrar_usuario(request):

    serializer = RegistroSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(
            {
                "mensaje": "Usuario creado correctamente."
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# ==========================================================
# LISTAR TODOS
# ==========================================================

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_articulos(request):

    articulos = Articulo.objects.filter(
        autor=request.user
    )

    serializer = ArticuloSerializer(
        articulos,
        many=True
    )

    return Response(serializer.data)


# ==========================================================
# DETALLE
# ==========================================================

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_articulo(request, pk):

    articulo = get_object_or_404(
        Articulo,
        pk=pk,
        autor=request.user
    )

    serializer = ArticuloSerializer(
        articulo
    )

    return Response(serializer.data)


# ==========================================================
# CREAR
# ==========================================================

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def api_crear(request):

    serializer = ArticuloSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save(
            autor=request.user
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# ==========================================================
# EDITAR
# ==========================================================

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def api_editar(request, pk):

    articulo = get_object_or_404(
        Articulo,
        pk=pk,
        autor=request.user
    )

    serializer = ArticuloSerializer(
        articulo,
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# ==========================================================
# ELIMINAR
# ==========================================================

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def api_eliminar(request, pk):

    articulo = get_object_or_404(
        Articulo,
        pk=pk,
        autor=request.user
    )

    articulo.delete()

    return Response(
        {
            "mensaje": "Artículo eliminado."
        }
    )