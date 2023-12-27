from django import template
from  pages.models import Pages


regitser = template.Library()

@regitser.simple_tag(name='get_page_list')
def get_page_list():
  pages =  Pages.objects.all()
  return pages

