
from django.http import JsonResponse

def index(request):
    """
    View function for the index page.
    """
    # Example logic: Retrieve some data
    data = {'message': 'Welcome to the backend app!'}

    # Return a JSON response
    return JsonResponse(data)
