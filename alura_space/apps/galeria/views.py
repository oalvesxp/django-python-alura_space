from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar este recurso.')   
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data").filter(publicada=True)

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar este recurso.')   
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data").filter(publicada=True)

    if "buscar" in request.GET:
        palavra = request.GET['buscar']
        if palavra:
            fotografias = fotografias.filter(nome__icontains=palavra)
    
    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar este recurso.')   
        return redirect('login')

    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post realizado com sucesso')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass