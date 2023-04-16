from django.urls import path

from api.views import TaskAPIView, ProjectAPIView, StatusAPIView, TypeAPIView

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task_api_view'),
    path('tasks/<int:pk>', TaskAPIView.as_view(), name='task_api_detail'),
    path('projects/', ProjectAPIView.as_view(), name='projects_api_view'),
    path('projects/<int:pk>', ProjectAPIView.as_view(), name='projects_api_detail'),
    path('statuses/', StatusAPIView.as_view(), name='status_api_view'),
    path('statuses/<int:pk>', StatusAPIView.as_view(), name='status_api_detail'),
    path('types/', TypeAPIView.as_view(), name='type_api_view'),
    path('types/<int:pk>', TypeAPIView.as_view(), name='type_api_detail'),
]
