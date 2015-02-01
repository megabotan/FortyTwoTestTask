from django.conf import settings


def pass_settings(request):
    return {'settings': settings}
