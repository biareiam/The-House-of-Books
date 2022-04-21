from django.shortcuts import render


def view_bag(request):
    """ View basket """
    return render(request, 'bag/bag.html')

