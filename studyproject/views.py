from django.shortcuts import render


def index(request):
    """首页视图"""
    return render(request, 'study_index/index.html')