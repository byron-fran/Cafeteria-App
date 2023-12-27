from .models import Pages

def cxt_dict(request):

    pages = Pages.objects.all()

    return {'pages': pages}