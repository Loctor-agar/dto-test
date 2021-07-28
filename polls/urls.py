from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.employee),
    path("position/", views.PositionList.as_view()),
    path("position/v2/", views.PositionListv2.as_view()),
    path("positions/<int:pk>/", views.PositionDetail.as_view()),
    path("positions/v2/<int:pk>/", views.PositionDetailv2.as_view()),
]