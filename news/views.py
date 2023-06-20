from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Todo.objects.all()
    return render(request, 'news/news.html', {'news': news})

class NewsDetail(DetailView):
    model = Todo
    template_name = 'news/detail.html'
    context_object_name = 'todo'

class NewsUptade(UpdateView):
    model = Todo
    template_name = 'news/create.html'
    form_class = TodoForm

class NewsDelete(DeleteView):
    model = Todo
    success_url = '/news/'
    template_name = 'news/news_delete.html'

    def post(self, request, *args, **kwargs):
        # Логика удаления новости
        return self.delete(request, *args, **kwargs)

def create(request):
    error = ''
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "your form don't work"


    form = TodoForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request,'news/create.html', data)