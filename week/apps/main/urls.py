from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import WeekView, index

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('week/', WeekView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
