from .models import Category, Technicians, Service

def category_list(request):
    categories = Category.objects.all()
    return {'categories' : categories}

def team_list(request):
    technicians = Technicians.objects.all()
    return {'technicians' : technicians}

def service_list(request):
    services = Service.objects.all()
    return {'services' : services}

