from django.urls import path
from django.views.generic.base import TemplateView

from .views import tail_log

urlpatterns = [
    path('<str:container_name>', TemplateView.as_view(template_name='tail_docker_logs/index.html'), name='index'),
    path('docker/logs/<str:container_name>', tail_log, name='tail_log'),
]
