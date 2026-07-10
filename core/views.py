from django.shortcuts import render

def home(request):
    """Renders the primary landing page of SafeRoute BD."""
    return render(request, 'core/home.html')