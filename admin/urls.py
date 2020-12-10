from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'admin'

urlpatterns = [
    # ------------------------------ 민우
    # 메인화면
    path('', views.index, name='index'),
    # 재직 선생님
    path('teacher.in', views.teacher_in, name='teacherin'),
    # 퇴원 선생님
    path('teacher.out', views.teacher_out, name='teacherout'),
    # 선생님 상세
    path('teacher_detail/<int:teacher_tbl_t_no>', views.teacher_detail, name='teacher_detail'),
    # 재원생 목록
    path('student.in', views.student_in, name='studentin'),
    # 퇴원생 목록
    path('student.out', views.student_out, name='studentout'),
    # 학생 상세
    path('student_detail/<int:c_no>', views.student_detail, name='student_detail'),
    # 강의 목록
    path('lecture', views.lecture_create, name='lecture_create'),
    # 학부모 목록
    path('parents_list', views.parents_list, name='parents_list'),
    # 로그인(관리자)
    path('login', views.login_admin, name='login_admin'),
    # 로그아웃(관리자)
    path('logout', views.logout_admin, name='logout_admin'),
    # 상담 목록
    path('consult_list', views.consult_list, name='consult_list'),
    # 사용자 페이지 관리
    path('userpage', views.userpage, name='userpage'),
    # 차트 데이터 json
    path('chart.data/', views.chart_data, name = 'chart_data'),
    # url(r'^chart.data$', views.chart_data, name = 'chart_data'),
    #-----------------------------------------------------병훈
    path('notice', views.notice, name='notice'),
    path('faq', views.faq, name='faq'),
    path('noticelist', views.noticelist, name='noticelist'),
    # path('test', views.test, name='test'),
    # path('testtest', views.testtest, name='testtest'),
    path('noticedetail/<int:notice_tbl_t_no>', views.noticedetail, name='noticedetail'),
    # path('noticedetail/modify/<int:notice_tbl_t_no/',views.detail_modify,name='detail_modify'),
    # path('noticedetail/delete/<int:notice_tbl_t_no>/', views.detail_delete, name='detail_delete'),
    path('faqlist', views.faqlist, name='faqlist'),
    # path('faqlist/<int:faq_no>', views.faqlist_detail, name='faqlist'),



]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)