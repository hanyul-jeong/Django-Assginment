from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path, include
from fake_db import user_db
from todo.views import todo_list, todo_info, todo_create, todo_update, todo_delete
from users import views as users_views
from todo.cb_views import (
    TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView
)
from django.contrib.auth.views import LogoutView

_db = user_db

def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in _db.items()]
    return render(request, 'todo/../templates/user_list.html', {'data': names})

def user_info(request, user_id):
    if user_id > len(_db):
        raise Http404('User not found')
    info = _db[user_id]
    return render(request, 'todo/../templates/user_info.html', {'data': info})

urlpatterns = [
    path('cbv/todo/', TodoListView.as_view(), name='cbv_todo_list'),
    path('cbv/todo/create/', TodoCreateView.as_view(), name='cbv_todo_create'),
    # URL 패턴의 이름을 'todo_info'로 변경하여 템플릿과 일치시킵니다.
    path('cbv/todo/<int:pk>/', TodoDetailView.as_view(), name='todo_info'),
    path('cbv/todo/<int:pk>/update/', TodoUpdateView.as_view(), name='cbv_todo_update'),
    path('cbv/todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='cbv_todo_delete'),

    path('cbv/accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('cbv/logout/', LogoutView.as_view(), name='logout'),
]
