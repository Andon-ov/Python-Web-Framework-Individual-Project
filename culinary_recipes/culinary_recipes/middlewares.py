from django.http import Http404


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 500:
            raise Http404
        return response
    return middleware
