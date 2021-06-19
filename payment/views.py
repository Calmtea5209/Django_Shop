from django.shortcuts import render,get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from order.models import Order

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id = order_id)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL, #電子郵件
        'amount': '%.2f' % order.total_cost(),
        'item_name': '編號{}'.format(order.id), #品項名稱
        'invoice': str(order.id), #發票編碼
        'currency_code': 'TWD', #貨幣編碼 ISO-4217標準
        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')), #付費狀況通知
        'return_url': 'http://{}{}'.format(host,reverse('payment:done')), #完成後返回
        'cancel_return': 'http://{}{}'.format(host,reverse('payment:canceled')), #取消後返回
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request,'payment/process.html',{'order':order,'form':form})

@csrf_exempt
def payment_done(request):
    return render(request,'payment/done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request,'payment/canceled.html')

# Create your views here.
