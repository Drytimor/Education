from django.urls import path
from . import views as weekdays



urlpatterns = [
    path('', weekdays.main_to_do_list),
    path('<int:week_days>/', weekdays.to_do_list_num),
    path('<str:week_days>/', weekdays.to_do_list, name='days_name'),

]