from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path, include
from fake_db import user_db
from todo.views import todo_list, todo_info
from users import views as users_views



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
    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', users_views.login, name='login'),
    path('accounts/signup/', users_views.sign_up, name='signup')
]
