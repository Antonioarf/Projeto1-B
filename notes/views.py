from django.shortcuts import render, redirect
from .models import Note

#################################################
def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')

        if isinstance(request.POST.get('apagar'), str):
            Note.objects.filter(id=int(request.POST.get('apagar'))).delete()

        elif isinstance(request.POST.get('atualizar'), str):
            Note.objects.filter(id=int(request.POST.get('atualizar'))).update(title = title,content = content)
        
        else:
            Note.objects.create(title = title,content = content, tag = tag)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})
#################################################

def meio(request):
    if request.method == 'POST':
        tag = request.POST.get('tag')
        return redirect('lista')
    else:
        lista = Note.objects.values_list("tag", flat = True).distinct()
        return render(request, 'notes/lista.html',{"tags": lista})

#################################################


def back_final(request):
    if request.method == 'POST':
        tag = request.POST.get('tag')
        return redirect('final', tag = tag)
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/final.html', {'notes': all_notes})
        # .filter(user = user)
#################################################

def carrega(request,tag):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')


        if isinstance(request.POST.get('apagar'), str):
            Note.objects.filter(id=int(request.POST.get('apagar'))).delete()

        elif isinstance(request.POST.get('atualizar'), str):
            Note.objects.filter(id=int(request.POST.get('atualizar'))).update(title = title,content = content)
        
        else:
            Note.objects.create(title = title,content = content, tag = tag)
        return redirect('final', tag = tag)
    else:
        all_notes = Note.objects.filter(tag = tag).all()
        return render(request, 'notes/final.html', {'notes': all_notes, "tagg": tag})
#################################################

def volta(request):
    if request.method == 'POST':
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})