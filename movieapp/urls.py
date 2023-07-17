from django.urls import path, include

from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.home, name='home'),
    # path('<int:movie_id>/', views.detail, name='detail'),
    # path('rate/<int:movie_id>/', views.rate, name='rate'),
    # path('recommendations/', views.recommendations, name='recommendations'),
    path('about/', views.about, name='about')
]