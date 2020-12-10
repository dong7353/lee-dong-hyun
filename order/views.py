from django.shortcuts import render
from admin.models import *

# Create your views here.

from django.http import HttpResponse


def order(request):
    lecture_list = lecture_tbl.objects.order_by
    context = {'lecture_list' : lecture_list}
    return render(request, 'order/order.html', context)