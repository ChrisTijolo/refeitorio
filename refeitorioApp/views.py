from django.shortcuts import render, get_object_or_404, redirect
from refeitorioApp.forms import AlunoForms, EventoForms
from refeitorioApp.models import Aluno, Evento


# Create your views here.
def home(request):
    form = AlunoForms()
    context = {'form': form}
    return render(request, 'refeitorio/home.html', context)

def evento(request):
    form = EventoForms()
    context = {'form': form}
    return render(request, 'refeitorio/evento.html', context)

def new_aluno(request):
    alunos=Aluno.objects.all()
    form = AlunoForms(request.POST, request.FILES)
    if request.method =="POST":
        if form.is_valid():
            aluno=form.save()
            aluno.save()
            form=AlunoForms()
    context={'form':form, 'alunos':alunos}
    return render(request, 'refeitorio/new_aluno.html', context)

def editar_aluno(request, id):
    alunos = Aluno.objects.all()
    aluno = get_object_or_404(Aluno, pk=id)
    form= AlunoForms(instance=aluno)
    if (request.method=='POST'):
        form = AlunoForms(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('new_aluno')
        else:
            return render(request, 'refeitorio/editar_aluno.html',{'form':form,'alunos':alunos})
    else:
        return render(request, 'refeitorio/editar_aluno.html',{'form':form})

def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForms(instance=aluno)
    alunos=Aluno.objects.all()
    if(request.method == "POST"):
        aluno.delete()
        return redirect('new_aluno')
    return render(request, 'refeitorio/excluir_aluno.html', {'aluno':aluno, 'alunos':alunos, 'form':form})

def new_evento(request):
    eventos = Evento.objects.all()
    form = EventoForms(request.POST, request.FILES)
    if request.method =="POST":
        if form.is_valid():
            evento =form.save()
            evento.save()
            form=EventoForms()
    context={'form':form, 'eventos':eventos}
    return render(request, 'refeitorio/new_evento.html', context)

def editar_evento(request, id):
    eventos = Evento.objects.all()
    evento = get_object_or_404(Evento, pk=id)
    form= EventoForms(instance=evento)
    if (request.method=='POST'):
        form = EventoForms(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('new_evento')
        else:
            return render(request, 'refeitorio/editar_evento.html',{'form':form,'eventos':eventos})
    else:
        return render(request, 'refeitorio/editar_evento.html',{'form':form})

def excluir_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)
    form = EventoForms(instance=evento)
    eventos=Evento.objects.all()
    if(request.method == "POST"):
        evento.delete()
        return redirect('new_evento')
    return render(request, 'refeitorio/excluir_evento.html', {'evento':evento, 'eventos':eventos, 'form':form})