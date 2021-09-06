'''''
from django.urls import path
from . import views

app_name = 'App_Login'
'''''
'''''
urlpatterns = [
    
    path('sign_up/', views.show_admin_sign_up, name='sign_up_page_admin'),
    path('admin_sign_up/', views.add_admin_sign_up, name='admin_sign_up'),
    path('manager_sign_up/', views.add_manager_sign_up, name='manager_sign_up'),
    path('show_manager_sign_up/', views.show_manager_sign_up, name='manager_sign_up_view'),
    path('login_view/', views.show_login_page, name='login_view'),
    path('login_page/', views.login_page, name='LoginPage'),
    
]
'''
'''''
urlpatterns = [
    path('admin_registration/', views.admin_register, name='admin_register'),
    path('manager_registration/', views.manager_register, name='manager_register'),
    path('employee_registration/', views.employee_register, name='employee_register'),
    path('user_login/', views.user_login, name='user_login'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

'''


from django.urls import path
from . import new_views, admin_views, manager_views, employee_views

app_name = 'App_Login'

urlpatterns = [
    path('signup/admin/', new_views.AdminSignUpView.as_view(), name='admin_signup'),
    path('signup/manager/', new_views.ManagerSignUpView.as_view(), name='manager_signup'),
    path('signup/employee/', new_views.EmployeeSignUpView.as_view(), name='employee_signup'),
    path('user_login/', new_views.user_login, name='user_login'),
    path('login/', new_views.login_page, name='login'),
    path('profile/admin/', admin_views.Profile.as_view(), name='admin_profile'),
    path('index/admin/', admin_views.index, name='index'),
    path('profile/manager/', manager_views.Profile.as_view(), name='manager_profile'),
    path('index/manager/', manager_views.index, name='manager_index'),
    path('profile/employee/', employee_views.EmployeeProfile.as_view(), name='employee_profile'),
    path('index/employee/', employee_views.index, name='employee_index'),
    path('employee_details/', admin_views.employee_view, name='employee'),
    path('manager_details/', admin_views.manager_view, name='manager'),
    path('logout/', new_views.logout_user, name='logout'),
    path('test/', new_views.test, name='test'),
    #admin dashboard
    path('home/', admin_views.admin_dashboard, name='admin_main_home'),
]

