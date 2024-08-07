from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='mypost'),
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.BlogUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.BlogDeleteView.as_view(), name='post-delete'),
    path('generate/', views.BlogGenerate.as_view(), name='gen'),
]
