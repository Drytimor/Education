from django.shortcuts import render


def table(requests):
    return render(requests, 'table/beautiful_table.html')
