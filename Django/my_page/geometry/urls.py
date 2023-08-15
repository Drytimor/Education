from django.urls import path
from geometry import views

urlpatterns = [
    # path('rectangle/<int:width>/<int:length>', views.rectangle, name='rectangle_name'),
    # path('square/<int:width>', views.square, name='square_name'),
    # path('circle/<int:circle>', views.circle, name='circle_name'),
    path('rectangle/', views.rectangle),
    path('square/', views.square),
    path('circle/', views.circle),
    path('get_rectangle_area/<int:width>/<int:length>', views.get_rectangle_area),
    path('get_square_area/<int:width>', views.get_square_area),
    path('get_circle_area/<int:circle>', views.get_circle_area),
]