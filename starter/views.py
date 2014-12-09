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
	year_list = []
	mpaa_rating_list = []
	runtime_list = []
	release_dates_list = []
	ratings_list = []
	synopsis_list = []
	actors_list = []
	characters_list = []
	posters_list = []
	for x in range(0,13):
		title_list.append(values['movies'][x]['title'])
		year_list.append(values['movies'][x]['year'])
		mpaa_rating_list.append(values['movies'][x]['mpaa_rating'])
		runtime_list.append(values['movies'][x]['runtime'])
		release_dates_list.append(values['movies'][x]['release_dates']['theater'])
		ratings_list.append(values['movies'][x]['ratings'])
		synopsis_list.append(values['movies'][x]['synopsis'])
		actors_list.append(values['movies'][x]['abridged_cast'][0]['name'] + "   ")
		#characters_list.append(values['movies'][x]['abridged_cast']['characters'])
		posters_list.append(values['movies'][x]['posters']['thumbnail'])
	#return HttpResponse(json.dumps(title_list, indent=1))
	return HttpResponse(actors_list)