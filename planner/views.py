from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from planner.models import Planner
from graphos.sources.simple import SimpleDataSource
from graphos.renderers import flot

def studyplanner(request):
	if request.method == "POST":
		days = int(request.POST.get('days'))
		subjects = request.POST.get('subjects')
		sub1 = request.POST.get('sub1')
		subhour1 = float(request.POST.get('subhour1', 0))
		sub2 = request.POST.get('sub2')
		subhour2 = float(request.POST.get('subhour2', 0))
		sub3 = request.POST.get('sub3')
		subhour3 = float(request.POST.get('subhour3', 0))
		sub4 = request.POST.get('sub4')
		subhour4 = float(request.POST.get('subhour4', 0))
		sub5 = request.POST.get('sub5')
		subhour5 = float(request.POST.get('subhour5', 0))
		sub6 = request.POST.get('sub6')
		subhour6 = float(request.POST.get('subhour6', 0))
		totalhours = float(subhour1 + subhour2 + subhour3 + subhour4 + subhour5 + subhour6)
		dataset = [["Days", "No. of hours to study per day"]]
		for i in range(days+1,0,-1):
			if i <=2:
				hours = totalhours/i
				dataset.append([-i,hours])
			else:
				hours = totalhours/(i)
				dataset.append([-i,hours])
		
		data_source = SimpleDataSource(data=dataset)

		chart = flot.LineChart(data_source)

		if days <= 2 :
			studyhours = totalhours/(days)
		else:
			studyhours = totalhours/(days)
		
		hours = int(studyhours)
		minutes = (studyhours*60) % 60
		#seconds = (studyhours*3600) % 60
		return render(request, 'planner/studyplanner.html', {"hours": hours, "minutes": int(minutes), "chart":chart, "days":days, "subjects":subjects})

	return render(request, 'planner/studyplanner.html')

