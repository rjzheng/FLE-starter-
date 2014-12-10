from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

def landing_page(request):
    return render(request, "starter/landing_page.html")

def json_read(request):
	jsonFile = open("starter/data/movies.json", 'r')
	values = json.load(jsonFile)
	title = values['movies'][1]['title']
	jsonFile.close()

	movie_list = []

	for x in range(0,13):
		title = values['movies'][x]['title']
		year = values['movies'][x]['year']
		runtime = values['movies'][x]['runtime']
		release_dates = values['movies'][x]['release_dates']['theater']
		critics_score = values['movies'][x]['ratings']['critics_score']
		audience_score = values['movies'][x]['ratings']['audience_score']
		synopsis = values['movies'][x]['synopsis']
		thumbnail = values['movies'][x]['posters']['thumbnail']
		movie = {
			'title' : title,
			'year' : year,
			'runtime' : runtime,
			'release_dates' : release_dates,
			'critics_score' : critics_score,
			'audience_score' : audience_score,
			'synopsis' : synopsis,
			'thumbnail' : thumbnail
		}
		movie_list.append(movie)

	return render_to_response('starter/base.html', {'movie_list': movie_list})


