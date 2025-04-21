from django.shortcuts import render
from .forms import TagForm

def tag_form(request):
    form = TagForm()
    return render(request, 'myapp/tag_form_3.html', {
        'form': form
    })