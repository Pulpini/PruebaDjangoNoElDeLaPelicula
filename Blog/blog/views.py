from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Consulta
from .forms import ConsultaForm


# DASHBOARD PSICOLÓGICO
@login_required
def dashboard(request):
    consultas = Consulta.objects.filter(psicologo=request.user).order_by('-fecha_creacion')

    total = consultas.count()

    ansiedad = consultas.filter(estado_emocional='Ansiedad').count()
    depresion = consultas.filter(estado_emocional='Depresión').count()

    return render(request, 'blog/dashboard.html', {
        'consultas': consultas,
        'total': total,
        'ansiedad': ansiedad,
        'depresion': depresion
    })


# LISTA
@login_required
def lista_consultas(request):
    consultas = Consulta.objects.all().order_by('-fecha_creacion')

    return render(request, 'blog/lista.html', {
        'consultas': consultas
    })


# DETALLE
@login_required
def detalle_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)

    return render(request, 'blog/detalle.html', {
        'consulta': consulta
    })


# CREAR
@login_required
def crear_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)

        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.psicologo = request.user
            consulta.save()

            return redirect('lista_consultas')

    else:
        form = ConsultaForm()

    return render(request, 'blog/form.html', {
        'form': form,
        'titulo': 'Registrar Consulta Psicológica'
    })


# EDITAR
@login_required
def editar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)

    form = ConsultaForm(request.POST or None, instance=consulta)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lista_consultas')

    return render(request, 'blog/form.html', {
        'form': form,
        'titulo': 'Editar Consulta'
    })


# ELIMINAR
@login_required
def eliminar_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)

    if request.method == 'POST':
        consulta.delete()
        return redirect('lista_consultas')

    return render(request, 'blog/confirmar-eliminar.html', {
        'consulta': consulta
    })


# LOGIN SIMPLE
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'blog/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')