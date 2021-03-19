from django.shortcuts import render, redirect
from .models import Dojos, Ninjas

def index(request):
    context = {
        "all_dojos": Dojos.objects.all(),
        "all_ninjas": Ninjas.objects.all()
    }
    return render(request, 'index.html', context)

def process_dojo(request):
    name = request.POST['dojo_name']
    city = request.POST['city']
    state = request.POST['state']
    Dojos.objects.create(name = name, city = city, state = state)
    return redirect('/')

def process_ninja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo = request.POST['dojo']
    Ninjas.objects.create(dojo = Dojos.objects.get(id=dojo), first_name = first_name, last_name = last_name)
    return redirect('/')

def delete(request):
    dojo_id = request.GET['id_to_delete']
    dojo_to_delete = Dojos.objects.get(id = dojo_id)
    dojo_to_delete.delete()
    return redirect('/')
