from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView, DeleteView
from .models import Todo

class TodoListView(ListView):
    model = Todo

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
    
    
                           
# Você pode manter a função `todo_list_old` para referência, mas não é mais necessária:
def todo_list_old(request):
    nome = 'Rodrigo'
    alunos = ['1. Ana', '2. José', '3. Bia']
    return render(request, "todos/todo_list.html", {"nome": nome, "lista_alunos": alunos})

# View para listar todos os todos
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})

