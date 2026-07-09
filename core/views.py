from django.shortcuts import render


def health_check(request):
    """Temporary view to verify project setup and routing."""
    return render(request, 'base.html')