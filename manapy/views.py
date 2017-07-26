from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
# Create your views here.

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404
    return HttpResponse(view_redirection)

def list_articles(request, year, month):
    # Il veut des articles ? Soyons fourbe et redirigeons-le vers djangoproject.com
    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def date_actuelle(request):
    return render(request, 'test/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'test/addition.html', locals())
