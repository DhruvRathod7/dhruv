from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>/', CustomerAPI.as_view()),
    path('get/', get),
    path('get/<int:id>', get),
    path('create/',create),
    path('delete/<int:id>/', delete),
    path('update/<int:id>/', patch),

]