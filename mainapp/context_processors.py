from .models import Category, Technicians

def category_list(request):
    categories = Category.objects.all()
    return {'categories' : categories}

def team_list(request):
    technicians = Technicians.objects.all()
    return {'technicians' : technicians}

