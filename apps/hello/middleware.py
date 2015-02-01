from models import Request


class RequestMiddleware():
    def process_request(self, request):
        r = Request(url=request.path, method=request.method)
        r.save()
