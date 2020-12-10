from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template.loader import render_to_string

from  .forms import *
from admin.models import *
from django.views.generic import View


import json
from django.core.serializers.json import DjangoJSONEncoder

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import threading

class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        msg.send(self.fail_silently)

def send_mail(subject, recipient_list, body='', from_email='<네이버 메일계정>', fail_silently=False, html=None, *args, **kwargs):
    EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()




class find(View):
    template_name = 'find/ID_find.html'
    form = RecoveryIdForm


    def get(self, request):
        if request.method=='GET':
            form = RecoveryIdForm(request.GET)
        return render(request, self.template_name, { 'form':form, })

def ajax_find_id_view(request):
    c_name = request.POST.get('c_name')
    c_phone = request.POST.get('c_phone')
    result_id = find.objects.get(c_name=c_name, c_id=c_phone)

    return HttpResponse(json.dumps({"result_id": result_id.user_id}, cls=DjangoJSONEncoder),
                        content_type="application/json")


from .forms import RecoveryPwForm

class RecoveryPwView(View):
    template_name = 'find/PW_find.html'
    recovery_pw = RecoveryPwForm

    def get(self, request):
        if request.method=='GET':
            form = self.recovery_pw(None)
            return render(request, self.template_name, { 'form':form, })

from .views import EmailThread

def ajax_find_pw_view(request):
    c_id= request.POST.get('user_id')
    target_user = models.objects.get(c_id=c_id)

    if target_user:
        auth_num = EmailThread()
        target_user.auth = auth_num
        target_user.save()

        send_mail(
            '비밀번호 찾기 메일입니다.{c_pw}',format(c_pw),
            [email],
        )
    return HttpResponse(json.dumps({"result": target_user.user_id}, cls=DjangoJSONEncoder), content_type = "application/json")


def auth_confirm_view(request):
    c_id = request.POST.get('c_id')
    input_auth_num = request.POST.get('input_auth_num')
    target_user = models.objects.get(c_id=c_id, auth=input_auth_num)
    target_user.auth = ""
    target_user.save()
    request.session['auth'] = target_user.user_id

    return HttpResponse(json.dumps({"result": target_user.user_id}, cls=DjangoJSONEncoder),
                        content_type="application/json")
