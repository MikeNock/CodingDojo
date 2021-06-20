from django.shortcuts import render, redirect, HttpResponse
def index(request):
    if request.method == "GET":
        return render(request,'survey.html')
    if request.method == "POST":
        context = {
            request.session['name'] == request.POST['name'],
            request.session['location'] == request.POST['location'],
            request.session['languages'] == request.POST['languages'],
            request.session['comment'] == request.POST['comment']
        }
        return render(request, "result.html", context)
    return render(request, 'result.html')