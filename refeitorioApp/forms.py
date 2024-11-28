from refeitorioApp.models import Aluno, Evento
from django import forms

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"

class EventoForms(forms.ModelForm):
    class Meta:
        model = Evento
        fields = "__all__"