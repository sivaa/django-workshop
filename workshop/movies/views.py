from django.shortcuts import render

def movies(request):
        return render(request, "movies.html")
