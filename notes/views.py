from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        if isinstance(request.POST.get('apagar'), str):
            Note.objects.filter(id=int(request.POST.get('apagar'))).delete()

        elif isinstance(request.POST.get('atualizar'), str):
            Note.objects.filter(id=int(request.POST.get('atualizar'))).update(title = title,content = content)
        
        else:
            Note.objects.create(title = title,content = content)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})