from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:name_slug>', views.pages, name='page'),
]
