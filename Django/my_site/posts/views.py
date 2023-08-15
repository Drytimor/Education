from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def name_posts(requests, name_posts):
    data = {
        'name': name_posts
    }
    return render(requests, 'posts/detail_by_name.html', context=data)

def number_posts(requests, num_posts):
    data = {
        'number': num_posts
    }
    return render(requests, 'posts/detail_by_number.html', context=data)

def posts(requests):
    return render(requests, 'posts/list_detail.html')