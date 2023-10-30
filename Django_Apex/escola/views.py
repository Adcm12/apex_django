
from rest_framework import viewsets
from escola.models import Aluno, Curso
from .serializer import AlunoSerializer, CursoSerializer

from django.shortcuts import render
from django.http import JsonResponse


def alunos(request):
    if request.method == 'GET':
        aluno = {'Id: ': 1, 'Nome: ': 'Seu Nome'}
        return JsonResponse(aluno)

class AlunosViewSets(viewsets.ModelViewSet):
    "Exibindo todos os Cursos"
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSets(viewsets.ModelViewSet):
    "Exibindo todos os Cursos"
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer



# Create your views here.
