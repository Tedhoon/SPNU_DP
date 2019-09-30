from django.shortcuts import render , get_object_or_404
from .models import *

# Create your views here.
def delivery(request):
    delivery_lists = DeliveryList.objects.all()
    return render(request, 'delivery.html', {'delivery_lists' : delivery_lists})


def delivery_list(request , list_id):
    list_details = get_object_or_404(DeliveryList, pk=list_id)

    return render(request , 'delivery_list.html' , {'list_details' : list_details})


# def delivery_modal(request , list_id):
#     list_details = get_object_or_404(DeliveryList, pk= list_id)
#     return render()