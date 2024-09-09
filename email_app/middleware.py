from django.utils.deprecation import MiddlewareMixin

class FixedCsrfMiddleware(MiddlewareMixin):
    def process_request(self, request):
        fixed_csrf_token = 'adfafafasasfasfassdsd'
        request.META['CSRF_COOKIE'] = fixed_csrf_token
        request.META['CSRF_COOKIE_USED'] = True
        request.META['CSRF_COOKIE'] = fixed_csrf_token  # Ensure it's set correctly in META
        request.COOKIES['csrftoken'] = fixed_csrf_token  # Set the token in the request cookies

    def process_response(self, request, response):
        response.set_cookie('csrftoken', 'adfafafasasfasfassdsd')
        return response