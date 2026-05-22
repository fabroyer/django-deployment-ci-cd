from django.shortcuts import render


def index(request):
    """
    Displays the index page.

    Parameters:
        request: HTTP request object, containing all request information.

    Returns:
        Renders HTTP response containing the HTML template.
     """
    return render(request, "index.html")


def sentry_debug(request):
    division_by_zero = 1 / 0
