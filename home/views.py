from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    """ Return the index page """

    paginate_by = 6

    return render(request, "home/index.html")
