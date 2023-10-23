from django.shortcuts import render
import time

class ShowDelayTemplateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Render the template.
        if not request.POST.get('pass', False):
            response = render(request, 'delay_template.html')
            return response

        # Proceed with the original response.
        response = self.get_response(request)

        return response