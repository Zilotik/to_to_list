from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TasksForm
from django.views.generic import DeleteView, DetailView


# Create your views here.
def main(request):
    tasks = Tasks.objects.all()
    context_object_name = 'tasks'
    return render(request, 'main/index.html', {'tasks' : tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной!'
        return redirect('main')

    form = TasksForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)


class BdDetailView(DetailView):
    model = Tasks
    template_name = 'main/detail_view.html'
    context_object_name = 'date'


class BDDeleteView(DeleteView):
    model = Tasks
    template_name = 'main/delete.html'
    success_url = f'/'
