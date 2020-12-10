from django.shortcuts import render, redirect
import bcrypt, random, string
from .forms import *
from admin.models import *
from django.utils import timezone
from django.contrib.auth.models import User, Group

# # 학생 회원가입
# def student_sign_up(request):
#     if request.method == "POST":
#         form = studentsignupform(request.POST)
#         if form.is_valid():
#             customer_tbl = form.save(commit=False)
#             customer_tbl.c_join = timezone.now()
#             customer_tbl.c_state = True
#             User.objects.create_user(username=customer_tbl.c_id, password=customer_tbl.c_pw)
#
#             # queryset = User.objects.order_by('-id')
#             # print(111,queryset[-1])
#
#             # 비밀번호 암호화
#             customer_tbl.c_pw = makeHashPassword(customer_tbl.c_pw)
#             # customer_tbl.user_id = User.objects.get()
#             # c_code 생성
#
#             random_code = ''
#             string_code = string.ascii_letters + string.digits
#
#             for i in range(6):
#                 random_code += random.choice(string_code)
#
#             customer_tbl.c_code = random_code
#             # db에 정보 저장
#             customer_tbl.save()
#             return redirect('/teacher')
#
#     else:
#         form = studentsignupform()
#
#     return render(request,'sign_up/c_signup.html',{'form':form})

# 학생 회원가입
def student_sign_up(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        # student_form = student_Form(request.POST)
        if user_form.is_valid():
            User = user_form.save()
            User.save()

            # username = request.POST['username']
            # password = request.POST['password']
            # User.objects.create_user(username=username, password=password)

            # customer_tbl.c_join = timezone.now()
            # customer_tbl.c_state = True
            # User.objects.create_user(username=customer_tbl.c_id, password=customer_tbl.c_pw)

            # queryset = User.objects.order_by('-id')
            # print(111,queryset[-1])

            # 비밀번호 암호화
            # customer_tbl.c_pw = makeHashPassword(customer_tbl.c_pw)
            # customer_tbl.user_id = User.objects.get()
            # c_code 생성

            # random_code = ''
            # string_code = string.ascii_letters + string.digits
            #
            # for i in range(6):
            #     random_code += random.choice(string_code)

            # customer_tbl.c_code = random_code
            # db에 정보 저장
            # customer_tbl.save()
            return redirect('/teacher')

    else:
        form = studentsignupform()
        user_form = UserForm()
        context = {'user_form' : user_form }
    return render(request,'sign_up/c_signup.html', context)



# 학부모 회원가입

def parent_sign_up(request):
    if request.method == "POST":
        form = parentsignupform(request.POST)
        if form.is_valid():
            customer_tbl = form.save(commit=False)
            customer_tbl.c_join = timezone.now()
            customer_tbl.c_state = True
            User.objects.create_user(username=customer_tbl.c_id, password=customer_tbl.c_pw)
            # 비밀번호 암호화
            customer_tbl.c_pw = makeHashPassword(customer_tbl.c_pw)

            # db에 정보 저장
            customer_tbl.save()
            return redirect('/teacher')

    else:
        form = parentsignupform()

    return render(request,'sign_up/c_signup.html',{'form':form})

# 선생님 회원가입

def teacher_sign_up(request):
    if request.method == "POST":
        form = teachersignupform(request.POST,request.FILES)
        if form.is_valid():
            teacher_tbl = form.save(commit=False)
            teacher_tbl.t_join = timezone.now()
            teacher_tbl.t_state = True
            User.objects.create_user(username=teacher_tbl.t_id, password=teacher_tbl.t_pw,first_name=teacher_tbl.t_name[0:1],last_name=teacher_tbl.t_name[1:],is_staff=True)

            # 비밀번호 암호화
            teacher_tbl.t_pw = makeHashPassword(teacher_tbl.t_pw)

            # db에 정보 저장

            teacher_tbl.save()
            return redirect('/teacher')

    else:
        form = teachersignupform()

    return render(request,'sign_up/t_signup.html',{'form':form})

# 비밀번호 암호화
def makeHashPassword(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashed.decode()

# 비밀번호 찾기 / 로그인 시 비밀번호 확인
def isPasswordCheck(hashed,password):
    return bcrypt.checkpw(password.encode('utf-8'),hashed.encode())


