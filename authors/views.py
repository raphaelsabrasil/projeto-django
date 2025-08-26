from django.shortcuts import render

from .forms import RegisterForm

# Create your views here.
def register_view(request):
    # return render(request, 'authors/pages/register_view.html')
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })