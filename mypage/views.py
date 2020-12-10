from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from admin.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#마이페이지 Default 페이지, 개인정보 수정 페이지
def mypage(request):
    # customer_info = customer_tbl.objects.get(pk=1)  # 사용자 정보 가져오기
    # user_info = User.objects.get(pk=1)
    # username = user_info.username
    # # context = { 'customer_info' : customer_info }

    if request.method == "POST":
        user_info = User.objects.get(pk=1)
        username = user_info.username
        password = request.POST['passwd']  # 입력한 비밀번호
        user = authenticate(username = username, password = password)
        context = {'user_info': user_info}

        if user is not None:
            #개인정보 수정페이지로...
            return render(request, 'mypage/information_insert.html', context)
        else:
            print('틀림')

    return render(request, 'mypage/checkpw.html')


# #마이페이지 출결현황
# def mypagecalendar(request):
#     return render(request, 'mypage/cal.html')

# Create your views here.
