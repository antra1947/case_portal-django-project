from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('cases/', views.case_list, name="case_list"),
    path('cases/<int:pk>/', views.case_detail, name="case_detail"),
    path('cases/add/', views.add_case, name="add_case"),
    path('cases/<int:case_id>/add_document/', views.add_document, name='add_document'),
    path('cases/<int:case_id>/add_hearing/', views.add_hearing, name='add_hearing'),
    path('notifications/', views.notifications, name='notifications'),
    path('login/', views.open_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
