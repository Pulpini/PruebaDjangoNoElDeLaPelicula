# Proyecto Blog Django

## Descripción

Este proyecto corresponde al desarrollo de un sistema CRUD utilizando Django y SQLite.

Permite administrar artículos mediante operaciones de creación, lectura, modificación y eliminación (CRUD).

El sistema incorpora autenticación de usuarios utilizando el sistema de autenticación nativo de Django.

---

# Objetivos

Desarrollar una aplicación web utilizando el framework Django aplicando la arquitectura MVT.

Implementar un CRUD funcional conectado a una base de datos SQLite.

Aplicar autenticación de usuarios.

Utilizar formularios mediante ModelForm.

---

# Tecnologías utilizadas

- Python 3
- Django
- SQLite3
- Bootstrap 5
- HTML5
- CSS
- Git
- GitHub

---

# Arquitectura utilizada

El proyecto utiliza la arquitectura MVT (Model View Template).

## Model

Representa la base de datos.

Archivo:

blog/models.py

---

## View

Contiene la lógica del programa.

Archivo:

blog/views.py

---

## Template

Representa la interfaz visual.

Carpeta:

templates/blog

---

# Funcionalidades

✔ Inicio de sesión

✔ Cerrar sesión

✔ Crear artículos

✔ Editar artículos

✔ Eliminar artículos

✔ Ver detalle

✔ Listado de artículos

✔ Administración mediante Django Admin

---

# Instalación

Crear entorno virtual

Windows

python -m venv venv

Activar entorno

venv\Scripts\activate

Instalar dependencias

pip install django

Migraciones

python manage.py makemigrations

python manage.py migrate

Crear administrador

python manage.py createsuperuser

Ejecutar proyecto

python manage.py runserver

Abrir navegador

http://127.0.0.1:8000

---

# Base de datos

SQLite3

Archivo

db.sqlite3

---

# CRUD

Create

Crear artículos.

Read

Visualizar artículos.

Update

Modificar artículos.

Delete

Eliminar artículos.

---

# Seguridad

Se utiliza

@login_required

para impedir que usuarios no autenticados modifiquen información.

También se utiliza

{% csrf_token %}

para prevenir ataques CSRF.

---

# Autor

Martín Rodríguez Pérez

TNS Informática mención Ciberseguridad

2026

https://github.com/Pulpini/PruebaDjangoNoElDeLaPelicula.git