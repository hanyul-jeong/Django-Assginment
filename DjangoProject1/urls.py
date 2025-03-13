from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path
from fake_db import user_db
from todo.views import todo_list, todo_info # 추가


_db = user_db


def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in _db.items()]
    return render(request, 'user_list.html', {'data': names})


def user_info(request, user_id):
    if user_id > len(_db):
        raise Http404('User not found')
    info = _db[user_id]
    return render(request, 'user_info.html', {'data': info})


urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", user_list, name="user_list"),
    path("users/<int:user_id>/", user_info, name="user_info"),

    path('todo/', todo_list, name='todo_list'),  # 추가
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),  # 추가
]
