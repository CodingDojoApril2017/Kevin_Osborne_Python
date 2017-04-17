from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "survey_form/index.html")

def result(request):

    return render(request, "survey_form/result.html")

def process(request):
    if 'count' in request.session:
        request.session['count'] +=1
    else:
        request.session['count'] = 0
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favlanguage'] = request.POST['favlanguage']
    request.session['comment'] = request.POST['comment']
    return redirect ('/result')
