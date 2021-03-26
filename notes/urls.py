from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/', views.meio, name='lista'),
    path('final/', views.back_final, name='final'),
    path('final/<str:tag>', views.carrega, name='final'),
    path('retorno/', views.volta, name='final'),

]
# <str:tag>