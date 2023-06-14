from django.urls import path
from .views import LededitApiView,LedCreateApiView

urlpatterns = [
    path('led-edit/<int:pk>',LededitApiView.as_view(),name="led-edit"),
    path('led-create/',LedCreateApiView.as_view(),name="led-create"),
]