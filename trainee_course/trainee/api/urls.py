from django.urls import path
from .views import *


urlpatterns = [
    path('api/trainee/', trainee_list, name='trainee-list'),
    path('api/', trainee_list, name='trainee-list'),
    path('api/trainee/<int:ID>/', trainee_detail, name='trainee-detail'),
    path('api/trainee/create/', TraineeCreate.as_view(), name='trainee-create'),
    path('api/trainee/update/<int:id>/', TraineeUpdate.as_view(), name='trainee-update'),
    path('api/trainee/delete/<int:id>/', TraineeDelete.as_view(), name='trainee-delete')
]