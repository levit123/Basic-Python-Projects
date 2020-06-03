from django.http import HttpResponse
from django.shortcuts import render


# view for the home page that is triggered when the user doesn't enter anything after the main website path
def home(request):
    user = request.user
    # dictionary object that will hold info to be used in the display page
    context = {
        'user': user,
    }
    # displays the "home.html" page, passing in the "context" dictionary object for it to use
    return render(request, "home.html", context)
