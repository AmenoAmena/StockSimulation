from django.shortcuts import render
from django.http import HttpResponse
from .prices import Price

# Create your views here.
def index(request):
    # Instantiate the Price class
    price_tracker = Price()
    
    # Fetch stock prices using the class methods
    google_price = price_tracker.google_price()
    apple_price = price_tracker.apple_price()
    microsoft_price = price_tracker.microsoft_price()
    amazon_price = price_tracker.amazon_price()
    tesla_price = price_tracker.tesla_price()
    nvidia_price = price_tracker.nvidia_price()
    visa_price = price_tracker.visa_price()
    coca_cola_price = price_tracker.coca_cola_price()
    intel_price = price_tracker.intel_price()
    meta_price = price_tracker.meta_price()

    # Render the template with stock prices
    return render(request, 'Content/index.html', {
        'google': google_price,
        'apple': apple_price,
        'microsoft': microsoft_price,
        'amazon': amazon_price,
        'tesla': tesla_price,
        'nvidia': nvidia_price,
        'visa': visa_price,
        'coca_cola': coca_cola_price,
        'intel': intel_price,
        'meta': meta_price,
    })