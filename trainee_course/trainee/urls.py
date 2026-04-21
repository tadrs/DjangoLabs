from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('trainee/', TraineeList, name='traineeList'),
    path('', TraineeList, name='traineeList'),
    path('trainee/<int:id>/', TraineeDetail, name='traineeDetail'),
    path('trainee/create/', TraineeCreate.as_view(), name='traineeCreate'),
    path('trainee/<int:id>/update/', TraineeUpdate.as_view(), name='traineeUpdate'),
    path('trainee/<int:id>/delete/', TraineeDelete.as_view(), name='traineeDelete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)