from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Renders a page displaying all Letting objects.

    Parameters:
        request: HTTP request object, containing all request information.

    Returns:
        Renders HTTP response containing the HTML page template and context data.
     """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Returns information about a Letting instance.

    Parameters:
        request: HTTP request object, containing all request information.
        letting_id: ID of the Letting instance from which data is retrieved.

    Returns:
        Renders HTTP response containing the HTML page template and context data.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
