from django.urls import path
from bug_app import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('login/', views.loginview, name = 'login'),
    path('logout/', views.logoutview, name = 'logout'),
    path('signup/', views.signupview, name = 'signup'),
    path('ticket_detail/<int:id>/', views.ticket_detail_view, name = 'ticket_detail'),
    path('assigning/<int:id>/', views.assigning_ticket_view, name = 'assigning'),
    path('completed/<int:id>/', views.completed_ticket_view, name = 'completed'),
    path('invalid/<int:id>/', views.invalid_ticket_view, name = 'invalid'),
    path('ticket_edit/<int:id>/', views.ticket_edit, name = 'edit'),
    path('user/<int:id>/', views.user_view, name = 'user'),
    path('add_ticket/', views.add_ticket, name = 'add'),
    ]