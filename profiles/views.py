from django.shortcuts import render
from .models import Profile


def index(request):
    """
     Renders the profiles list page with all Profile objects from the database.

    Parameters:
        request: HTTP request object, containing all request information.

    Returns:
        Renders HTTP response containing the HTML page template and context data.
     """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Renders the profile page for a user.

    Parameters:
        request: HTTP request object, containing all request information.
        username: Username associated with the Profile instance from which information is retrieved.

    Returns:
        Renders HTTP response containing the HTML page template and context data.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
