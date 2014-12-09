from django.shortcuts import render
from django.http import HttpResponse
import json

def landing_page(request):
    return render(request, "starter/landing_page.html")

def json_read(request):
	j = json.loads(open("starter/data/movies.json").read())
	return HttpResponse(json.dumps(j, indent=1), content_type="application/json")