from django.urls import path
from bug_app import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('signup/', views.signupview),
    path('ticket_detail/<int:id>/', views.ticket_detail_view),
    path('assigning/<int:id>/', views.assigning_ticket_view),
    path('completed/<int:id>/', views.completed_ticket_view),
    path('invalid/<int:id>/', views.invalid_ticket_view),
    path('ticket_edit/<int:id>/', views.ticket_edit),
    path('user_view/<int:id>/', views.user_view),
    ]