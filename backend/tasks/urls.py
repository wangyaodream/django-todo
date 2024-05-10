from django.urls import path, re_path

from . import views


# 定义命名空间，可以和其他app区分开
app_name = 'tasks'

urlpatterns = [
    # 创建任务url
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    # 获取任务列表
    path('', views.TaskListView.as_view(), name='task_list'),
    # 获取单一任务详情
    re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name="task_detail"),
    # update
    re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name="task_update"),
    # delete
    re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name="task_delete")
]
