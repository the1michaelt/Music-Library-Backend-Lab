from django.urls import path
from . import views

urlpatterns = [
    path('', views.songs_list),
    path('<int:pk>/', views.song_detail),
]


# path('',views.products_list),
# path('<int:pk>/', views.product_detail),
# my API to serve content on the following URLs paths:   Paths must match these exactly!   ‘api/music/'   ‘api/music/<int:pk>/’