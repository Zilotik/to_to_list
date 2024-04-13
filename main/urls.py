from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.BdDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', views.BDDeleteView.as_view(), name='delete')
]