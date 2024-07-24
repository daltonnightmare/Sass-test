import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
def home(request, *args, **kwargs):
	pagevisit = PageVisit.objects.all()
	creation = PageVisit.objects.create()
	titre = "willy"
	context = {
		'PageVisit':pagevisit,
		'nbr': pagevisit.count(),
		'titre': titre
	}
	return render(request, 'index.html', context)


"""
this_dir = pathlib.Path(__file__).resolve().parent
def home(request, *args, **kwargs):
	print(this_dir)
	html_ = ''
	html_file = this_dir/'index.html'
	html_ = html_file.read_text()
	return HttpResponse(html_)"""