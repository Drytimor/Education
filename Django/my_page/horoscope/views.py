from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

horoscope_dict = {
    'fire': {
        "aries": (1, "aries", "Овен - первый знак зодиака, планета Марс", {3: (21, 32), 4: (1, 21)}),
        "leo": (5, "leo", "Лев - пятый знак зодиака, солнце", {7: (23, 32), 8: (1, 24)}),
        "sagittarius": (9, "sagittarius", "Стрелец - девятый знак зодиака, планета Юпитер", {11: (23, 31), 12: (1, 22)}),
    },
    'earth': {
        "taurus": (2, "taurus", "Телец - второй знак зодиака, планета Венера", {4: (21, 31), 5: (1, 22)}),
        "virgo": (6, "virgo", "Дева - шестой знак зодиака, планета Меркурий", {8: (25, 32), 9: (1, 23)}),
        "capricorn": (10, "capricorn", "Козерог - десятый знак зодиака, планета Сатурн",  {12: (22, 32), 1: (1, 21)}),
    },
    'air': {
        "gemini": (3, "gemini", "Близнецы - третий знак зодиака, планета Меркурий", {5: (22, 32), 6: (1, 22)}),
        "libra": (7, "libra", "Весы - седьмой знак зодиака, планета Венера", {9: (23, 31), 10: (1, 24)}),
        "aquarius": (11, "aquarius", "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн", {1: (21, 32), 2: (1, 19)}),
    },
    'water': {
        "cancer": (4, "cancer", "Рак - четвёртый знак зодиака, Луна", {6: (22, 31), 7: (1, 23)}),
        "scorpion": (8, "scorpion", "Скорпион - восьмой знак зодиака, планета Марс", {10: (24, 32), 11: (1, 23)}),
        "pisces": (12, "pisces", "Рыбы - двенадцатый знак зодиака, планеты Юпитер", {2: (19, 29), 3: (1, 21)}),
    },
}

def your_zodiac(requests, month, day):
    redirect_url = None
    for i in horoscope_dict.values():
        for j in i.values():
            for key_month, value_day in j[3].items():
                if month == key_month and day in range(*value_day):
                    redirect_url = reverse('horoscope-name', args=[j[1]])
    if redirect_url is None:
        return HttpResponse('Введите корректную дату')
    return HttpResponseRedirect(redirect_url)



def type_elements(requests, element):
    data = {}
    for sign in horoscope_dict[element]:
        data.setdefault('name', []).append(sign)
    return render(requests, 'horoscope/type_elements.html', context=data)


def type_(requests):
    data = {}
    for elem in horoscope_dict:
        data.setdefault('name', []).append(elem)
    return render(requests, 'horoscope/element.html', context=data)

def index(requests):
    data = {}
    for sing in horoscope_dict.values():
        for zodiac in sing.keys():
            data.setdefault('name', []).append(zodiac)
    return render(requests, 'horoscope/index.html', context=data)


def info_sing_horoscope(requests, sing_zodiac):
    navbar = []
    for i in horoscope_dict.values():
        for j in i.values():
            navbar.append(j[1])

    for elem in horoscope_dict.values():
        info_zodiac = elem.get(sing_zodiac)
        if info_zodiac is not None:
            data = {
                'description': info_zodiac[2],
                'name': info_zodiac[1],
                'navbar': navbar
            }
            return render(requests, 'horoscope/info_zodiac.html', context=data)
    return HttpResponseNotFound(f'Неизвестный знак зодиака - {sing_zodiac}')



def info_num_horoscope(requests, sing_zodiac: int):
    if sing_zodiac > 12:
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sing_zodiac}')
    for elem in horoscope_dict.values():
        for sing in elem.values():
            if sing_zodiac == sing[0]:
                name_zodiac = sing[1]
                redirect_urls = reverse('horoscope-name', args=[name_zodiac])
                return HttpResponseRedirect(redirect_urls)


def my_float_converters(requests, sing_zodiac):
    return HttpResponse(f'{sing_zodiac}')

def my_split_converter(requests, sing_zodiac):
    return HttpResponse(f'{sing_zodiac}')

def my_upper_converters(requests, sing_zodiac):
    return HttpResponse(f"{sing_zodiac}")




