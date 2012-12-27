from pruebas.models import MenuItem
from django.views.generic.simple import direct_to_template 
def main(request):
    menu_items = MenuItem.objects.all()
    return direct_to_template(request, 'main.html', {'menu_items': menu_items})
