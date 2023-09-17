from django.shortcuts import render
from item.models import Category , Item
from django.shortcuts import render, redirect
from .forms import SignInForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold =False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories':categories,
        'items':items,
    })

def contact(request):
    return render(request, 'core/contact.html')
 
def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')  # Replace 'home' with the appropriate URL name
    else:
        form = SignInForm()
    return render(request, 'core/sign_in.html', {'form': form})

    