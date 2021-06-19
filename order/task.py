from django.core.mail import send_mail

from .models import Order


def order_created(order_id): #寄送email
    order = Order.objects.get(id=order_id)
    subject = '訂單編號 {}'.format(order.id)
    message = '親愛的 {}, 你好\n\n您已成功建立此訂單.\
                您的訂單編號為 {}.'.format(order.first_name,order.id)
    mail_sent = send_mail(subject,
                          message,
                          'willy5209593@gmail.com',
                          [order.email])
    return mail_sent
