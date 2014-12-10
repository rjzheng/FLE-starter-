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

	title_list = []
	year_list = []
	mpaa_rating_list = []
	runtime_list = []
	release_dates_list = []
	ratings_list = []
	synopsis_list = []
	critics_rating_list = []
	critics_score_list = []
	audience_score_list = []	
	actors_list = []
	characters_list = []
	posters_list = []
	for x in range(0,13):
		title_list.append(values['movies'][x]['title'])
		year_list.append(values['movies'][x]['year'])
		mpaa_rating_list.append(values['movies'][x]['mpaa_rating'])
		runtime_list.append(values['movies'][x]['runtime'])
		release_dates_list.append(values['movies'][x]['release_dates']['theater'])
		critics_score_list.append(values['movies'][x]['ratings']['critics_score'])
		audience_score_list.append(values['movies'][x]['ratings']['audience_score'])
		synopsis_list.append(values['movies'][x]['synopsis'])
		#actors_list.append(values['movies'][x]['abridged_cast'][0]['name'] + "   ")
		#characters_list.append(values['movies'][x]['abridged_cast'][0]['characters'])
		posters_list.append(values['movies'][x]['posters']['thumbnail'])
	#return HttpResponse(json.dumps(title_list, indent=1))
	return render_to_response("starter/base.html", {'title': title_list[0], 'poster': posters_list[0],
	 						  'year': year_list[0], 'ratings': mpaa_rating_list[0],
	 						  'runtime': runtime_list[0],'critics_score': critics_score_list[0],
	 						  'audience_score': audience_score_list[0], 'release_dates': release_dates_list[0],
	 						  'synopsis': synopsis_list[0]})


