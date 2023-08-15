from django.urls import path
from posts import views

urlpatterns = [
    path('<int:num_posts>/', views.number_posts),
    path('<name_posts>/', views.name_posts),
    path('', views.posts)
]

