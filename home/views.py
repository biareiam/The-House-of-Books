from django.shortcuts import render


def index(request):
    """ Return the index page """

    paginate_by = 6

    return render(request, "home/index.html")
