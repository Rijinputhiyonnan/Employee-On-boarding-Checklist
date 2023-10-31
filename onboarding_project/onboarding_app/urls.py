from django.urls import path

from onboarding_app import views

urlpatterns = [
   
    path("", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path('logout/', views.logout_view, name='logout'),
    path("employees", views.employee_list, name="employee_list"),
    path("employees/<int:pk>/", views.employee_detail, name="employee_detail"),
    path("employees/create/", views.employee_create, name="employee_create"),
    
    path("employees/<int:pk>/update/", views.employee_update, name="employee_update"),

    path("employees/<int:pk>/delete/", views.employee_delete, name="employee_delete"),
    path("employees/<int:pk>/mark_onboarded/", views.employee_mark_onboarded, name="employee_mark_onboarded"),
    path('base/', views.base, name='base'),
    
    
]
