from django.shortcuts import render

def home(request):
	# define homepage for joshagby.com
	options = {}
	return render(request, 'personalSiteDjango/home.html', options)