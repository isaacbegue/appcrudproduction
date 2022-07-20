from django.shortcuts import redirect, render
from .forms import TareaForm
from .models import Tarea

# Create your views here.

def home(request):
    tareas = Tarea.objects.all()
    content = {'tareas': tareas}
    return render(request, 'appCRUD/home.html', content)

def agregar(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    content = {'form': form}
    return render(request, 'appCRUD/agregar.html', content)

def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("home")

def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm(instance=tarea)
    content = {'form': form}
    return render(request, 'appCRUD/editar.html', content)