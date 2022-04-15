from .models import Super_Type
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def super_types_list(request):
    pass 

@api_view(['GET', 'PUT', 'DELETE'])       
def super_type_detail(request, pk):
    pass
