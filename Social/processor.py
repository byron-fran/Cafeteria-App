from .models import Social

def cxt_dict(request):
    cxt = {}
    links = Social.objects.all()
    for link in links:
        cxt[link.key] = link.url
        
    return cxt