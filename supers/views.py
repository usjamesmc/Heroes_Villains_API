from .models import Super
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def supers_list(request):
    pass 

@api_view(['GET', 'PUT', 'DELETE'])       
def super_detail(request, pk):
    pass