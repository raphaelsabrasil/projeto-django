from django.shortcuts import render, redirect
from django.http import Http404

from .forms import RegisterForm

# Create your views here.
def register_view(request):     # para exibir os dados no formulário
    # return render(request, 'authors/pages/register_view.html')   
    # request.session['number']  = request.session.get('number') or 1
    # request.session['number'] += 1
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })

def register_create(request):   # para tratar os dados
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    return redirect('authors:register')

    # return render(request, 'authors/pages/register_view.html', {
    #     'form': form,
    # })