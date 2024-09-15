from django.shortcuts import render, redirect
from . import views

# Create your views here.
def index(request):
    context = {
        'title': 'AutoVox'
    }
    context['users'] = 5530
    context['servers'] = 5
    context['commands'] = 23
    return render(request, 'index.html', context)

def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'about.html', context)

def invite(request):
    # Redirect to the bot invite link
    return redirect('https://discord.com/oauth2/authorize?client_id=1281554625744470127&permissions=8&integration_type=0&scope=bot')

def support(request):
    # Redirect to the support server invite
    return redirect('https://discord.gg/8HbjJBGWBd')

def terms(request):
    context = {
        'title': 'Terms of Service'
    }
    return render(request, 'terms.html', context)

def privacy(request):
    context = {
        'title': 'Privacy Policy'
    }
    return render(request, 'privacy.html', context)

def soon(request):
    context = {
        'title': 'Coming Soon'
    }
    return render(request, 'soon.html', context)
