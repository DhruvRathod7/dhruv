from django.urls import path

from .views import (
    OrderAPI,
    patch,
    get,
    OrderDetailAPI,
    patch_detail,
    get_detail,
    create,
    create_detail,
    delete,
    delete_detail,
)
urlpatterns = [
    path('<int:pk>/', OrderAPI.as_view()),
    path('get/', get),
    path('get/<int:id>', get),
    path('create/',create),
    path('delete/', delete),
    path('update/<int:id>/', patch),
    path("detail/<int:id>/", OrderDetailAPI.as_view()),
    path("detail/get/", get_detail),
    path("detail/get/<int:id>", get_detail),
    path("detail/create/", create_detail),
    path("detail/delete/", delete_detail),
    path("detail/update/<int:id>/", patch_detail),

]