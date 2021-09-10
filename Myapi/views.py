import json 
from . import api
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, "index.html")

def get_json(request):
	if(request.method=='GET'):
		S = request.GET['username']
		T1 = request.GET['from']
		T2 = request.GET['to']
		N = request.GET['cnt']
		ProblemList = [ i.strip() for i in request.GET['list'].split(',') ]
		try:
			dit = api.get_data(S, T1, T2, N, ProblemList)
			response = json.dumps({'status':'OK','handle':S,'contestId':ProblemList[0][:-1],'results':dit})
		except:
			response = json.dumps([{ 'status': 'ERROR', 'results': 'No results found' }])
		return HttpResponse(response, content_type='text/json')