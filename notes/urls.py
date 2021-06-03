from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here

    path('api/users/', views.api_users),
    path('api/share/', views.api_share),

    path('tags/', views.meio, name='lista'),
    path('final/', views.back_final, name='final'),
    path('final/<str:tag>', views.carrega, name='final'),
    path('retorno/', views.volta, name='final'),

]
# <str:tag>