from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>/', ItemAPI.as_view()),
    path('get/', get),
    path('get/<int:id>', get),
    path('create/',create),
    path('delete/', delete),
    path('update/<int:id>/', patch),

]