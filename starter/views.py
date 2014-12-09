from django.shortcuts import render
from django.http import HttpResponse
import json

def landing_page(request):
    return render(request, "starter/landing_page.html")

def json_read(request):
	jsonFile = open("starter/data/movies.json", 'r')
	values = json.load(jsonFile)
	title = values['movies'][1]['title']
	jsonFile.close()

	title_list = []
	for x in range(0,13):
		title_list.append(values['movies'][x]['title'])
	#return HttpResponse(json.dumps(title_list, indent=1))
	return HttpResponse(title_list)