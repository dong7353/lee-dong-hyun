from django.shortcuts import render, redirect
from django.http import HttpResponse
from admin.models import *
import json

from django.views import View
from django.http import JsonResponse
from .models import customer_tbl

class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        customer_tbl(
            user_id = data['c_id'],
            user_pw = data['c_pw'],
        )

        if customer_tbl.objects.filter(user_id=data['c_id']).exists() == True:
            return JsonResponse({"message": "이미 존재하는 아이디입니다."}, status=401)

        else:
            customer_tbl.objects.create(user_id=data['c_id'], user_pw=data['c_pw'])
            return JsonResponse({"message": "회원으로 가입되셨습니다."}, status=200)
    def get(self, request):
        users = customer_tbl.object.values()
        return JsonResponse({"data" : list(users)}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        customer_tbl(
            user_id=data['c_id'],
            user_pw=data['c_pw'],
        )
        if customer_tbl.objects.filter(user_id=data['c_id'], user_pw=data['c_pw']).exists() == True:
            return JsonResponse({"message": "로그인에 성공하셨습니다."}, status=200)
        else:
            return JsonResponse({"message": "아이디나 비밀번호가 일치하지 않습니다."}, status=401)

    def get(self, request):
        user = customer_tbl.objects.values()
        return JsonResponse({"list": list(user)}, status=200)

#메인페이지 비로그인 상태 보이기
def mainpage(request):
    teacher_list = teacher_tbl.objects.all()
    lecture_list = lecture_tbl.objects.all()

    # 한명의 객체 뽑을 때
    # teacher = teacher_tbl.objects.get(t_no = 13)

    context = {'teacher_list': teacher_list, 'lecture_list': lecture_list}

    return render(request, 'mainpage/introduce.html', context)


############ 동현

def faq_list(request):
    faqlist = faq_tbl.objects.all()

    context = { 'faq_list' : faqlist }

    return render(request, 'mainpage/FrequentlyAskedQuestions.html', context)

def teacher_list(request):
    teacher_list = teacher_tbl.objects.all()
    lecture_list = lecture_tbl.objects.all()

    # 한명의 객체 뽑을 때
    # teacher = teacher_tbl.objects.get(t_no = 13)

    context = { 'teacher_list' : teacher_list, 'lecture_list' : lecture_list}

    return render(request, 'mainpage/introduce.html', context)

def notice_list(request):

    # 공지 구분이 전체인 경우만 출력하기 위해 filter를 걸어준다.
    notice_list = notice_tbl.objects.filter(notice_target = '전체')

    context = { 'notice_list' : notice_list }

    return render(request, 'mainpage/notice.html', context)

def notice_list2(request, notice_no):
    notice_list2 = notice_tbl.objects.get(notice_no = notice_no)

    context = { 'notice_list2' : notice_list2 }

    return render(request, 'mainpage/notice2.html', context)

def lecture_list(request):

    lecture_list = lecture_tbl.objects.all()

    context = { 'lecture_list' : lecture_list }

    return render(request, 'mainpage/lecture.html', context)

def Recruitment(request):
    return render(request, 'mainpage/Recruitment.html')




# #마이페이지 출결현황
# def mypagecalendar(request):
#     return render(request, '/index.html')




# Create your views here.

