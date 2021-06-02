from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
    
    path('api/users/', views.api_users),
    path('api/share/', views.api_share),

    path('tags/', views.meio, name='lista'),
    path('final/', views.back_final, name='final'),
    path('final/<str:tag>', views.carrega, name='final'),
    path('retorno/', views.volta, name='final'),

]
# <str:tag>