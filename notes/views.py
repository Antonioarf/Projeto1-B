from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import get_user_model



# SUAS OUTRAS FUNÇÕES CONTINUAM AQUI

@api_view(['GET', 'POST'])
def api_users(request):
    User = get_user_model()
    users = [u.username for u in User.objects.all()]
    print(type(users))
    print(users)
    return Response(users)


@api_view(['GET', 'POST'])
def api_share(request):
    User = get_user_model()
    users = [u.username for u in User.objects.all()]
    print(type(users))
    print(users)
    if request.method == 'POST':
        print(request.POST)
    return Response(users)

#################################################

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

#################################################

def index(request):
    # print("11111111111111111111")
    User = get_user_model()
    users = User.objects.all()
    # for u in users:
    #     print(u)
    # print('111111111111111111111')
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        prazo_html = request.POST.get('prazo')
        prazo_list = prazo_html.split("-")
        try:
            user = request.user.username
        except:
            user = "erro"
        if prazo_html == "":
            prazo_html = "Sem Prazo"

        if isinstance(request.POST.get('apagar'), str):
            Note.objects.filter(id=int(request.POST.get('apagar'))).delete()
        
        elif isinstance(request.POST.get('status'), str):

            atual = Note.objects.filter(id=int(request.POST.get('status'))).values("feito")[0]['feito']
            print(atual)
            Note.objects.filter(id=int(request.POST.get('status'))).update(feito = (not atual))
        
        elif isinstance(request.POST.get('atualizar'), str):
            Note.objects.filter(id=int(request.POST.get('atualizar'))).update(title = title,content = content, prazo= prazo_html)
        
        else:
            Note.objects.create(title = title,content = content, tag = tag, prazo = prazo_html)
            obj = Note.objects.last()
            obj.users.add(User.objects.get(username = user))
        return redirect('index')
    else:
        try:
            user = request.user.username
            all_notes = Note.objects.filter(users = User.objects.get(username = user))
        except:
            all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

#################################################

def meio(request):
    print("22222222222222222222222222222222")
    if request.method == 'POST':
        tag = request.POST.get('tag')
        return redirect('lista')
    else:
        lista = Note.objects.values_list("tag", flat = True).distinct()
        if len(lista)==0:
            erros = "Nenhuma Tag Criada"
        else:
            erros = ""
        
        return render(request, 'notes/lista.html',{"tags": lista, "erro":erros})

#################################################


def back_final(request):
    print("33333333333333333333333333333333")
    if request.method == 'POST':
        tag = request.POST.get('tag')
        return redirect('final', tag = tag)
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/final.html', {'notes': all_notes})
        # .filter(user = user)

#################################################

def carrega(request,tag):
    print("444444444444444444444444444444444444")
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        prazo_html = request.POST.get('prazo')
        prazo_list = prazo_html.split("-")

        print(request.POST)
        if prazo_html == "":
            prazo_html = "Sem Prazo"

        if isinstance(request.POST.get('apagar'), str):
            Note.objects.filter(id=int(request.POST.get('apagar'))).delete()

        elif isinstance(request.POST.get('status'), str):
            atual = Note.objects.filter(id=int(request.POST.get('status'))).values("feito")[0]['feito']
            print(atual)
            Note.objects.filter(id=int(request.POST.get('status'))).update(feito = (not atual))
        
        elif isinstance(request.POST.get('atualizar'), str):
            Note.objects.filter(id=int(request.POST.get('atualizar'))).update(title = title,content = content, prazo= prazo_html)
        
        else:
            Note.objects.create(title = title,content = content, tag = tag)
        return redirect('final', tag = tag)
    else:
        all_notes = Note.objects.filter(tag = tag).all()
        return render(request, 'notes/final.html', {'notes': all_notes, "tagg": tag})

#################################################

def volta(request):
    print("55555555555555555555555555555555")
    if request.method == 'POST':
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})