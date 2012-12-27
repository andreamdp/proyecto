from pruebas.models import MenuItem
def menu(request):
    tr =""
    for o in MenuItem.objects.all():
	tr +=o.descripcion + "  "      
    return{'menu':tr}
      
