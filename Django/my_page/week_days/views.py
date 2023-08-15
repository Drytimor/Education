from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

to_do_dict = {
    'monday': 'учиться_1',
    'tuesday': 'учиться_2',
    'wednesday': 'учиться_3',
    'thursday': 'учиться_4',
    'friday': 'учиться_5',
    'saturday': 'учиться_6',
    'sunday': 'выходной'
}

def to_do_list(requests, week_days):
    weekdays = to_do_dict.get(week_days)
    if weekdays:
        return HttpResponse(weekdays)
    return HttpResponseNotFound(f'на {week_days} ничего нет')

def to_do_list_num(requests, week_days):
    list_week_days = list(to_do_dict)
    if week_days > len(to_do_dict):
        return HttpResponseNotFound(f'Неверный номер дня - {week_days}')
    name_days = list_week_days[week_days - 1]
    redirect_url = reverse('days_name', args=[name_days])
    return HttpResponseRedirect(redirect_url)

def main_to_do_list(requests):
    return render(requests, 'week_days/greeting.html')

