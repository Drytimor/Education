from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# def rectangle(requests, width, length):
#     return HttpResponse(f'Площадь прямоугольника размером {width}x{length} равна {width*length}')
#
# def square(requests, width):
#     return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')
#
# def circle(requests, circle):
#     return HttpResponse(f'Площадь круга радиуса {circle} равна {circle**2 * 3.14}')


def rectangle(requests):
    return render(requests, 'geometry/rectangle.html')

def square(requests):
    return render(requests, 'geometry/square.html')

def circle(requests):
    return render(requests, 'geometry/circle.html')


def get_rectangle_area(requests, width, length):
    redirect_urls = reverse('rectangle_name', args=(width, length))
    return HttpResponseRedirect(redirect_urls)

def get_square_area(requests, width):
    redirect_urls = reverse('square_name', args=(width,))
    return HttpResponseRedirect(redirect_urls)

def get_circle_area(requests, circle):
    redirect_urls = reverse('circle_name', args=(circle,))
    return HttpResponseRedirect(redirtct_urls)
